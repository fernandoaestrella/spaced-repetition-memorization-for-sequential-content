# spaced_repetition_memorization_for_sequential_content
A tool to help you memorize long sequential content like text more efficiently using the spaced repetition technique

## Note:
Only works as expected in Windows

## Instructions:
1. Place the long text you want to review on a file called 'input.txt' in the same folder as this program
2. Run the program

It will save the state of all sections of text automatically after every evaluation of how easy it was to recall

When opening the program again, it will try to find a file called "state.txt". If it's found, it will load the last state from that file.

## Example output when reviewing a section of text:

The current section of text is:

===============================================================================================================================
[Current section of text goes here]
===============================================================================================================================Index: 96/100. Ease: 2.7

After you have tried to recall the next section of text, please input one of these keys to evaluate how easy it was to recall the current section of text

From hardest to easiest,
n
m
,
.
/

Or press 'Z' to go back to the section of text which was hardest to recall, so far

Or press any of the letter keys to the left of the 'Y' or 'H' keys to go to the previous section of text 

Or press any of the letter keys to the right of the 'T' or 'G' keys to go to the next section of text    

Only the keys between 'N' and '/' modify the recording of the easiness of a given section

## Instructions inside the program

This is a tool to help you memorize long sequential content like text more efficiently using the spaced repetition technique.
1. You will first input the long text you want to memorize in a file called 'input.txt' placed in the same folder as this program. It will be split wherever there is a period.
2. You will then be presented with each section of the text, and you will try to remember what is the next section of text after that one.
3. You will then evaluate how easy it was to recall the next section by pressing one of these keys:\n\nn -> very hard to recall or failed to do so
m
,
.
/ -> very easy to recall
The more to the left is the key that you press, you would be indicating that it was hardest to recall the next section of text, and the more to the right you press a key, you would be indicating it was easiest.
4. You can then keep reviewing a few more sections, or you could then press a key to go back to the section of text that was most difficult to recall so far

This tool is just a support and a guidance. You could have achieved the same result applying this technique while reviewing the material by being aware of which section of text was hardest to recall, and going back to it periodically, with a longer period the easier it was