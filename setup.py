from cx_Freeze import setup, Executable

setup(
    name = "syback",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["argparse","textwrap","platform","sys","subprocess","os","time","pyodbc","xml.etree.cElementTree"],
        'include_msvcr': True,
    }},
    executables = [Executable("syback.py")]
    )