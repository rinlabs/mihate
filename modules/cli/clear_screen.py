from os import system, name


def clear():
    """Clears console screen"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
