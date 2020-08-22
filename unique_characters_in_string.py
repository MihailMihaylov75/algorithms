__author__ = 'Mihail Mihaylov'
import sys
import unittest


# Given string determine if it is compressed of unique characters
def find_unique_characters_in_str1(string):
    """"Find unique characters in string vol 1"""
    return len(set(string)) == len(string)


def find_unique_characters_in_str2(string):
    """"Find unique characters in string vol 2"""
    chars = set()
    for letter in string:
        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True


class TestUniqueCharacters(unittest.TestCase):
    """"Class to determine if string contains unique characters"""
    def test_unique_characters1(self):
        """"Test unique characters v1"""
        self.assertEqual(find_unique_characters_in_str1('abcd'), True)
        self.assertEqual(find_unique_characters_in_str1(''), True)
        self.assertEqual(find_unique_characters_in_str1('gaa'), False)

    def test_unique_characters2(self):
        """"Test unique characters v2"""
        self.assertEqual(find_unique_characters_in_str2('abcd'), True)
        self.assertEqual(find_unique_characters_in_str2(''), True)
        self.assertEqual(find_unique_characters_in_str2('gaa'), False)


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))
