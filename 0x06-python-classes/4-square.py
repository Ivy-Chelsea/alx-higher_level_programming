#!/usr/bin/python3
""" Class square that defines a square based on 3-square.py """


class Square:
    def ___init___(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

            def area(sefl):
                return self.__size * self.__size
