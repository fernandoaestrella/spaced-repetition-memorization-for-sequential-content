# Using the formula from here https://www.supermemo.com/en/blog/application-of-a-computer-to-improve-the-results-obtained-in-working-with-the-supermemo-method

# Imports
import msvcrt
import os
import sys
import json

# Definitions
state_file_name = "state.txt"

divider = "==============================================================================================================================="

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.ease = 2.5
        self.index = 0

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Node):
            return { "index": obj.index, "data": obj.data, "ease": obj.ease, "prev": obj.prev.index, "next": obj.next.index}
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def as_node(input_node):
    if 'data' in input_node:
        new_node = Node("")
        new_node.data = input_node.get('data')
        new_node.index = input_node.get('index')
        new_node.ease = input_node.get('ease')
        node_list.append(new_node)
        return new_node
    return None

def is_valid_key(user_key):
    if user_key in ["n", "m", ",", ".", "/", "z", "q", "w", "e", "r", "t", "y", "a", "s", "d", "f", "g", "y", "u", "i", "o", "p", "h", "j", "k", "l"]:
        return True
    else:
        return False

def keep_asking_until_right_key():
    user_key = ""
    trying = True

    while trying:
        print("\nAfter you have tried to recall the next section of text, please input one of these keys to evaluate how easy it was to recall the current section of text\n\nFrom hardest to easiest,\nn\nm\n,\n.\n/\n\nOr press 'Z' to go back to the section of text which was hardest to recall, so far\n\nOr press any of the letter keys to the left of the 'Y' or 'H' keys to go to the previous section of text\n\nOr press any of the letter keys to the right of the 'T' or 'G' keys to go to the next section of text\n\nOnly the keys between 'N' and '/' modify the recording of the easiness of a given section")
        user_key = str(msvcrt.getch().decode('utf-8'))
        print(user_key)
        if is_valid_key(user_key):
            trying = False
        else:
            print(divider + "Wrong key entered. Please press one of the correct keys.\n" + divider)
    
    return user_key

def do_while(condition, body):
    """Emulates a do-while loop in Python.

    Args:
        condition: A callable object that returns a boolean value.
        body: A callable object that represents the loop body.
    """
    current_input = ""
    do = True
    
    while do:
        current_input = body()
        do = condition()
    
    return current_input

def find_lowest_ease_node(head):
    min_node = head

    current_node = head
    while current_node.data != 'End':
        if current_node.ease < min_node.ease:
            min_node = current_node

        current_node = current_node.next

    return min_node

def convert_input_to_ease(value):
    match value:
        case "n":
            return 1
        case "m":
            return 2
        case ",":
            return 3
        case ".":
            return 4
        case "/":
            return 5
        case _:
            return None

# Instructions
print("\033c")
print(divider + "\n\nThis is a tool to help you memorize long sequential content like text more efficiently using the spaced repetition technique.\n\n1. You will first input the long text you want to memorize in a file called 'input.txt' placed in the same folder as this program. It will be split wherever there is a period.\n\n2. You will then be presented with each section of the text, and you will try to remember what is the next section of text after that one.\n\n3. You will then evaluate how easy it was to recall the next section by pressing one of these keys:\n\nn -> very hard to recall or failed to do so\nm\n,\n.\n/ -> very easy to recall\n\nThe more to the left is the key that you press, you would be indicating that it was hardest to recall the next section of text, and the more to the right you press a key, you would be indicating it was easiest.\n\n4. You can then keep reviewing a few more sections, or you could then press a key to go back to the section of text that was most difficult to recall so far\n\nThis tool is just a support and a guidance. You could have achieved the same result applying this technique while reviewing the material by being aware of which section of text was hardest to recall, and going back to it periodically, with a longer period the easier it was")
print("\nPress any key when you've placed a file called 'input.txt' with the contents of text you want to review in the same folder as this program\n")
msvcrt.getch()

# Input mode
input_text = ""
head = Node("")
current_node = Node("")
node_list = []

try:
    # Check if the state had been previously saved
    with open(state_file_name, "r", encoding="utf-8") as f:
        # If so, loads the state to the expected data structure
        json.loads(f.read(), object_hook=as_node)

        for node in node_list:
            if node.data == "Start":
                node.next = node_list[1]
                node.prev = node_list[node_list.__len__() - 1]
            elif node.data == "End":
                node.next = node_list[0]
                node.prev = node_list[node_list.__len__() - 2]
            else:
                node.next = node_list[node.index + 1]
                node.prev = node_list[node.index - 1]
        
        head = node_list[0]
        current_node = head
except FileNotFoundError:
    # The state file does not exist.
    print("The file 'state.txt' does not exist. Opening 'input.txt'\n")

    try:
        # Open the input file for reading.
        with open("input.txt", "r", encoding="utf-8") as f:
            # Read the contents of the file.
            input_text = f.read()

            # Print the contents of the file.
            print("The input text is:\n\n" + input_text)

            # Set up
            split_string = input_text.split(".")
            split_string.insert(0, "Start")
            split_string.append("End")
            head = Node(split_string.pop(0))
            current_node = head
            current_index = 0

            # Create linked list
            for section in split_string:
                current_node.index = current_index
                current_node.next = Node(section)
                current_node.next.prev = current_node
                node_list.append(current_node)
                current_node = current_node.next
                current_index += 1

            # Make the linked list circular
            current_node.next = head
            head.prev = current_node
            head.prev.index = current_index
            node_list.append(current_node)

            current_node = head
    except FileNotFoundError:
        # The file does not exist.
        print("The file 'input.txt' does not exist. Please create one and run this program again\nCurrent working directory: " + os.getcwd())
        input()
        quit()
    except Exception as e:
        # An unexpected error occurred.
        print(e)
        input()
        quit()
except Exception as e:
    # An unexpected error occurred.
    print(e)
    input()
    quit()

# Review mode
while(True):
    # Clear the terminal screen
    print("\033c")

    # Display current node and some data about it. The total number of nodes is increased by two to account for the Start and End nodes
    print("The current section of text is:\n\n" + divider + "\n" + current_node.data + "\n" + divider + "Index: " + str(current_node.index) + "/" + str(node_list.__len__() + 2) + ". Ease: " + str(current_node.ease))

    # Evaluate easiness of recall
    selected_key = keep_asking_until_right_key()
    if selected_key == "z":
        # Find the node that was hardest to recall
        current_node = find_lowest_ease_node(head)
    elif selected_key in ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g"]:
        current_node = current_node.prev
    elif selected_key in ["y", "u", "i", "o", "p", "h", "j", "k", "l"]:
        current_node = current_node.next
    else:
        current_ease = convert_input_to_ease(selected_key)    
        # Update easiness of recall of this node
        current_node.prev.ease = current_node.ease + ( 0.1 - ( 5 - current_ease ) * ( 0.08 + ( 5 - current_ease ) * 0.02 ) )

        # Save the current state of the linked list
        with open(state_file_name, "w", encoding="utf-8") as f:
            json.dump(node_list, f, cls=ComplexEncoder)

        # Update current node
        current_node = current_node.next