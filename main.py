import sys

from components.Utils import check_python_version

if __name__ == "__main__":
    if not check_python_version():
        from components.Menu import Menu
        Menu()