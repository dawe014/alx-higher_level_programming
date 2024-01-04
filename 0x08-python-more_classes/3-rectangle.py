#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
       
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
       
        return self.__width

    @width.setter
    def width(self, value):
      
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        
        return self.__height

    @height.setter
    def height(self, value):
        
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        
        return self.width * self.height

    def perimeter(self):
       
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def str(self):
        
        rect = []
        if self.height == 0 or self.width == 0:
            return ""
        for n in range(0, self.__height):
            rect.append("#" * self.__width)
            if n != self.__height - 1:
                rect.append('\n')
        return ''.join(rect)