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


def reverse_string_recursively(s):
    """Reverse string recursively"""
    if len(s) <= 1:
        return s

    return reverse_string_recursively(s[1:]) + s[0]


def string_permutation(s):
    """Permutation of given string """
    out = []
    # Base
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            # For every permutation resulting
            for perm in string_permutation(s[:1] + s[i+1:]):
                out += [let + perm]
    return out


def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i + 1:]):
                print(let)
                print('****')
                print(perm)
                # Add it to output
                out += [let + perm]

    return out


def rec_coin(target, coins):
    """
    INPUT: Target change amount and list of coin values
    OUTPUT: Minimum coins needed to make change

    Note, this solution is not optimized.
    """

    # Default to target value
    min_coins = target

    # Check to see if we have a single coin match (BASE CASE)
    if target in coins:
        return 1

    else:

        # for every coin value that is <= than target
        for i in [c for c in coins if c <= target]:

            # Recursive Call (add a count coin and subtract from the target)
            num_coins = 1 + rec_coin(target - i, coins)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins
