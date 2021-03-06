"""Misc file tests.

Made for Jython.
"""
from __future__ import with_statement
import os
import unittest
from test import test_support

class FileTestCase(unittest.TestCase):

    def tearDown(self):
        if os.path.exists(test_support.TESTFN):
            os.remove(test_support.TESTFN)

    def test_append(self):
        # http://bugs.jython.org/issue1466
        mode = 'ab'
        fp1 = open(test_support.TESTFN, mode)
        fp1.write('test1\n')
        fp2 = open(test_support.TESTFN, mode)
        fp2.write('test2\n')
        fp1.close()
        fp2.close()
        with open(test_support.TESTFN) as fp:
            self.assertEqual('test1\ntest2\n', fp.read())

    def test_appendplus(self):
        # regression with the test_append fix:
        # http://bugs.jython.org/issue1576
        with open(test_support.TESTFN, 'ab+') as fp:
            fp.write('test1\n')
            fp.seek(0)
            self.assertEqual(fp.read(), 'test1\n')


def test_main():
    test_support.run_unittest(FileTestCase)


if __name__ == '__main__':
    test_main()
