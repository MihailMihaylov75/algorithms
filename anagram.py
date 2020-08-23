__author__ = 'Mihail Mihaylov'


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
