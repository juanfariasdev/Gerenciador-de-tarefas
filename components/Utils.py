import os
import sys

def clear_console():
    os.system("cls" if os.name in ("nt", "dos") else "clear")

def check_python_version():
    if sys.version_info < (3, 10):
        sys.exit("Este script requer Python 3.10 ou superior!")
