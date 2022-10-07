#!/usr/bin/python3
"""
creatation of base
"""
class Base:
    """
    assigns a base id
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
