__author__ = 'Mihail Mihaylov'
import sys
import unittest


def is_anagram(word_one, word_two):
    """Chek if given two words are anagram"""
    word_one = word_one.replace(' ', '').lower()
    word_two = word_two.replace(' ', '').lower()
    return sorted(word_one) == sorted(word_two)


def is_anagram2(word_one, word_two):
    """Chek if given two words are anagram"""
    result = {}
    word_one = word_one.replace(' ', '')
    word_two = word_two.replace(' ', '')

    if len(word_one) != len(word_two):
        return False

    for letter in word_one:
        if letter in result:
            result[letter] += 1
        else:
            if letter:
                result[letter] = 1

    for letter in word_two:
        if letter in result:
            result[letter] -= 1
        else:
            result[letter] = 1

    for letter in result:
        if result[letter] != 0:
            return False
    return True


class testAnagrams(unittest.TestCase):
    """Class that test anagram"""

    def test_anagram(self):
        """Test first anagram function."""
        self.assertEqual(is_anagram('gogogo', 'gggooo'), True)
        self.assertEqual(is_anagram('a', 'b'), False)
        self.assertEqual(is_anagram('clint eastwood', 'old west action'), True)
        self.assertEqual(is_anagram(' ', ' '), True)

    def test_second_anagram(self):
        """Test second anagram function."""
        self.assertEqual(is_anagram2('gogogo', 'gggooo'), True)
        self.assertEqual(is_anagram2('a', 'b'), False)
        self.assertEqual(is_anagram2('clint eastwood', 'old west action'), True)
        self.assertEqual(is_anagram2(' ', ' '), True)


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))
