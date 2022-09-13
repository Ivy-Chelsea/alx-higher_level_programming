#!/usr/bin/python3


class Square:
    """ Square class defined
    Attributes:
    size (int): Size of square
    position (tuple): position of space and new lines
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes
        Args:
        size (int): size
        position(tuple): position
        Returns: None
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter of size
        Return: Size of Square
        """

    @size.setter
    def size(self, value):
        """ Setter of size
        Args: value (int): size
        Raises: TypeError is size not int
                ValueError if size is less than 0
                Returns: None
                """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
            else:
            self.__size = value

    @property
    def position(self):
        """ get position atrribute"""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tupke of 2 positive integers")
        swlf.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(se;lf.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
