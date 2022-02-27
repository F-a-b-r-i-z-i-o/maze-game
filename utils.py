import os


def clear_screen():
    """
    Clears the console
    """
    os.system("cls" if os.name == "nt" else "clear")
