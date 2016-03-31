#!/usr/bin/env python
# encoding: utf-8
# filename: test_some_thing.py


def test_some_thing():
    from proj.sub_package.some_module import SomeClass
    foo = SomeClass(10, 10)
    assert foo.norm() == 14.142135623730951

