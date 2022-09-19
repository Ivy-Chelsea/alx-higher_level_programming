#!/usr/bin/python3
"""Module 1-recatngle
Defines a Rectangle class
"""


class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance

        Args:
            value: width value, must be a positive integer
        """
        if not instance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of a Rectangle instance

        Args:
            value: height value, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
