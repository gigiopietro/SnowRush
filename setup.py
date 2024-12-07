from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="SnowRush",
    version="1.0",
    description="Snowboarding app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)