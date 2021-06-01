#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry():
    """ The BaseGeometry class"""

    def area(self):
        """ exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates value TypeError
        if value is NOT an integer
        the value passed is NOT greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
