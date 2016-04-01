#!/usr/bin/env python
# encoding: utf-8
# filename: some_module.pyx

from libc.math cimport sqrt


cdef inline double sqr(double val) except -1:
    """Return the square of a number"""
    return (val * val)


cdef class SomeClass:
    """
    Some Class description

    Args:
        a (double): A number a
        b (double): A number b

    Attributes:
        a (double): A number a
        b (double): A number b

    Examples:
        >>> from proj.sub_package.some_module import SomeClass
        >>> foo = SomeClass(10, 10)
        >>> foo.a
        10.0
    """
    def __init__(self, double a, double b):
        self.a = a
        self.b = b

    cpdef double norm(self):
        """
        norm function description

        Returns:
            (NoneType) None

        Examples:
            >>> from proj.sub_package.some_module import SomeClass
            >>> foo = SomeClass(10, 10)
            >>> foo.norm()
            14.142135623730951
        """
        return sqrt(sqr(self.a) + sqr(self.b))
