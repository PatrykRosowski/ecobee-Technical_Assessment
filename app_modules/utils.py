import os
import platform


def clear():
    ''' Clear the terminal screen. '''

    # Check the platform to determine the correct command
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')