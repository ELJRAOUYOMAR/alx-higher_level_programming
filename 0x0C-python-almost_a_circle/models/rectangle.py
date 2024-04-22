#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """get the  width of this rectangle"""
        
        return self.__width
    
    @width.setter
    def width(self, value):
        """set a value to the width of this rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        """get the  height of this rectangle"""
        
        return self.__height
    
    @height.setter
    def height(self, value):
        """set a value to the height of this rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")        
        
        self.__height = value

    @property
    def x(self):
        """get the  x of this rectangle"""
        
        return self.__x
    
    @x.setter
    def x(self, value):
        """set a value to the x of this rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        
        self.__x = value

    @property
    def y(self):
        """get the  y of this rectangle"""
        
        return self.__y
    
    @y.setter
    def y(self, value):
        """set a value to the y of this rectangle"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        
        self.__y = value

    def area(self):
        """get the area of this rectangle"""
        
        return self.width * self.height

    def display(self):
        """Display the rectangle with '#' symbols, considering x and y positions"""

        for _ in range(self.y):
            print()  # Print empty lines for y offset

        for _ in range(self.height):
            print(" " * self.x, end="")  # Print spaces for x offset
            print("#" * self.width)
    
    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
                format(type(self).__name__, self.id,
                       self.x, self.y, 
                       self.width, self.height) 

    
    

    


    
    