#!/usr/bin/python3
"""
Define Rectangle class
"""


class Rectangle:
    """Represent rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            [pr.append(str(self.print_symbol)) for j in range(self.__width)]
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
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        return(rect_2)

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
