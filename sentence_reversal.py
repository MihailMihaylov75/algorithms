__author__ = 'Mihail Mihaylov'
import sys
import unittest


def sentence_reversal1(sequence):
    """"Reverse sequence function v1"""
    return " ".join(reversed(sequence.split()))


def sentence_reversal2(sequence):
    """"Reverse sequence function v1"""
    return " ".join(sequence.split()[::-1])


class TestSentenceReversal(unittest.TestCase):
    """"Class to test Sentence Reversal"""
    def test_sentence_reversal1(self):
        """"Test sequence reversal1"""
        self.assertEqual(sentence_reversal1('    space before'), 'before space')
        self.assertEqual(sentence_reversal1('   Hello John    how are you   '), 'you are how John Hello')
        self.assertEqual(sentence_reversal1('1'), '1')

    def test_sentence_reversal2(self):
        """"Test sequence reversal2"""
        self.assertEqual(sentence_reversal1('    space before'), 'before space')
        self.assertEqual(sentence_reversal1('   Hello John    how are you   '), 'you are how John Hello')
        self.assertEqual(sentence_reversal1('1'), '1')


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))