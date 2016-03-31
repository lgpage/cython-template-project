#!/usr/bin/env python
# encoding: utf-8
# filename: test_docs.py
# !!! THIS FILE WAS AUTOMATICALLY GENERATED... DO NOT EDIT !!!

import doctest


def test_some_module():
    from proj.sub_package import some_module
    failures, tests = doctest.testmod(some_module, verbose=True)
    assert failures == 0
