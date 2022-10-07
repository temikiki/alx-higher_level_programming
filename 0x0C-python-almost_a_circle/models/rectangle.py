#!/usr/bin/python3
"""
initialisation of module
"""

from models.base import Base
"""
importing id initialized from  base 
"""
class Rectangle(Base):
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)

    @property
    def width(self):
        """get value of width"""
        return self._width
    
    @width.setter
    def width(self, Value):
        """set width, raise error if negative"""
        if Value >= 0:
            self._width = Value
        else:
            raise ValueError("width must be positive")

    @property
    def height(self):
        """get value of height"""
        return self._height
    
    @height.setter
    def height(self, Value):
        """ set value for height"""
        if Value >= 0:
            self._height = Value
        else:
            raise ValueError("height must be postive")
    @property
    def x(self):
        """get the value of x"""
        return self._x
    @x.setter
    def x(self, Value):
        """set the value of x"""
        if Value >= 0:
            self._x = Value
        
        else:
            raise ValueError("x must be postive")
    @property
    def y(self):
        """get the value of y"""
        return self.y 
    @y.setter
    def y(self, Value):
        """set value of y"""
        if value >= 0:
            self._y = Value
        else:
            raise ValueError("y must be positive")

