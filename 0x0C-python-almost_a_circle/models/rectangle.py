#!/usr/bin/python3
"""Module rectangle
Creates a Rectangle class, inheriting from Base
"""

import json
from models.base import Base


class Rectangle
"""Class describing a rectangle
Public instance method:
        - area()
        - display()
        - to_dictionary()
        - update()
    Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance

        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
        """

        sel.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute"""

        return self.__height

    @property
    def x(self):
        """Retyrieves the x attribute"""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""

        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.__width = value

    @height.setter
    def height(self, value):
        """Sets then height attribute"""
