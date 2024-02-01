#!/usr/bin/python3

"""Does stuff"""


def text_indentation(text):
    """Text indentation"""
    if type(text) != str:
        raise TypeError("text must be a string")

    newline = True
    for i in text:
        if i in ".?:":
            newline = True  # to take care of space after delimeters
            print(i)
            print()
        else:
            if i == "\n":
                print(i, end="")
                newline = True  # to take care of space after "\n"

            if newline is True:
                if i == " " or i == "\n":
                    continue
                else:
                    newline = False
            print(i, end="")
