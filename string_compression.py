__author__ = 'Mihail Mihaylov'

from collections import OrderedDict


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
