import unittest
import doctest

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite("sizer"))
    tests.addTests(doctest.DocTestSuite("roof_assessment"))
    return tests