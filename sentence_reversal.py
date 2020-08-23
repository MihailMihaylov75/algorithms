__author__ = 'Mihail Mihaylov'


def sentence_reversal1(sequence):
    """"Reverse sequence function v1"""
    return " ".join(reversed(sequence.split()))


def sentence_reversal2(sequence):
    """"Reverse sequence function v1"""
    return " ".join(sequence.split()[::-1])
