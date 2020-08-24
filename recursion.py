__author__ = 'Mihail Mihaylov'
import math


# In this case, we have: n + (n-1) + (n-2) + .... + 0
def recursive_sum(n):
    """Sum numbers from n to 1"""
    return 0 if n == 0 else n + recursive_sum(n-1)


# if n = 4321, return 4+3+2+1
def sum_func(n):
    """Returns the sum of all the individual digits in that integer"""
    return n if len(str(n)) == 1 else n % 10 + sum_func(math.floor(n / 10))


def word_split(phrase, list_of_word, output=None):
    """Determine if it is possible to split the string in a way in which words can be made from the list of words"""
    # if output is None initialize it
    if output is None:
        output = []

    for word in list_of_word:
        # if the word is found append it to the output
        if phrase.startswith(word):
            output.append(word)
            # recursively call the split function on the remaining portion of the phrase
            return word_split(phrase[len(word):], list_of_word, output)
    return output
