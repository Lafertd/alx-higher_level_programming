#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """Represent rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimieter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Return printable format"""
        if self.__width == 0 or self.__height == 0:
            return("")
        pr = []
        for i in range(self.__height):
            [pr.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                pr.append("\n")
        return("".join(pr))

    def __repr__(self):
        """Return string representation"""
        rep = "Rectangle(" + str(self.__width) + ", "
        rep += str(self.__height) + ")"
        return(rep)

    def __del__(self):
        """Print message for deletion"""
        print("Bye rectangle...")
