#!/usr/bin/python3
'''module for Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class, inherit from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize Square class'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''return size'''
        return self.width

    @size.setter
    def size(self, value):
        '''set size'''
        self.width = value
        self.height = value

    def __str__(self):
        '''return string representation of Square'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
