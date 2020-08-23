__author__ = 'Mihail Mihaylov'
import collections


# find the missing element in arr2
def finder(arr1, arr2):
    """Find the missing element in two lists"""
    arr1.sort()
    arr2.sort()

    for i, j in zip(arr1, arr2):
        if i != j:
            return i
    return arr1[-1]


def finder2(arr1, arr2):
    """Find the missing element in two lists using collections"""
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
