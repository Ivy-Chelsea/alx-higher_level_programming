#!/usr/bin/python3
""" Class square that defines a square by:(based on 1-square.py)
    private instance attribute: size """


class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
