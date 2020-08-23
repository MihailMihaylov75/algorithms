__author__ = 'Mihail Mihaylov'


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
