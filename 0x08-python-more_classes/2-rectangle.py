#!/usr/bin/python3
"""Module 2-rectangle
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
        """Retrieves Rectangle width instance"""
        return self.width

    @width.setter
    def width(self, value):
        """Sets Rectangle width instance

        Args:
            value: width value, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves Rectangle height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets Rectangle height instance

        Args:
            value: height value, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be a integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates Rectangle area instance

        Returns:
            Area of the rectangle, given by height * width
        """
        return self.__width * self.__height
    
    def Perimeter(self):
        """Calculates Rectangle Perimeter instance
        
        Return:
            Perimeter of rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
