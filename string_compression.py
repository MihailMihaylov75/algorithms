__author__ = 'Mihail Mihaylov'

from collections import OrderedDict

import sys
import unittest


def string_compression(string):
    """"Compress a string of single and double letters"""
    if not string:
        return ''

    result = OrderedDict()
    output = ''
    for letter in string:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    for k, v in result.items():
        output += k
        output += str(v)

    return output


class TestStringCompression(unittest.TestCase):
    """"Class to test string compression"""
    def test_string_compression(self):
        """"Test string compression"""
        self.assertEqual(string_compression(''), '')
        self.assertEqual((string_compression('AAAA')), 'A4')
        self.assertEqual(string_compression('AABBCC'), 'A2B2C2')
        self.assertEqual(string_compression('BaRdBP'), 'B2a1R1d1P1')


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))
