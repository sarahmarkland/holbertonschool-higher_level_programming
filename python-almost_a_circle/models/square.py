#!/usr/bin/python3
'''module for Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square class, inherit from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize Square class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''return string representation of Square'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
