from cx_Freeze import setup, Executable

setup(
    name="setup_script",
    version="0.1",
    description="My Python script",
    executables=[Executable("main.py")],
)