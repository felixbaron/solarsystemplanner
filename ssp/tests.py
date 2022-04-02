import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("sizer"))
    return tests