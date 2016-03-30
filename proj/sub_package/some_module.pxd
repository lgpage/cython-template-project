#!/usr/bin/env python
# encoding: utf-8
# filename: some_module.pxd


cdef inline double sqr(double val) except -1


cdef class SomeClass:
    cdef:
        readonly double a
        readonly double b

    cpdef double norm(self)
