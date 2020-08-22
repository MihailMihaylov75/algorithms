__author__ = 'Mihail Mihaylov'
import sys
import unittest
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


class TestPairSum(unittest.TestCase):
    """Test class for finder"""
    def test_pair_sum(self):
        self.assertEqual(finder([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6, 7]), 5)
        self.assertEqual(finder([1, 2, 3], [2]), 1)
        self.assertEqual(finder([7, 6, 5, 4], [5, 6, 4]), 7)

    def test_second_pair_sum(self):
        """Test class for finder 2"""
        self.assertEqual(finder2([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 6, 7]), 5)
        self.assertEqual(finder2([1, 2, 3], [2]), 1)
        self.assertEqual(finder2([7, 6, 5, 4], [5, 6, 4]), 7)


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))
