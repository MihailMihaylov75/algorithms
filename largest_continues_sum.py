__author__ = 'Mihail Mihaylov'
import sys
import unittest


def large_continues_sum(arr):
    if not len(arr):
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum


class TestLargestSum(unittest.TestCase):
    """"Class to test largest continues sum"""
    def test_pair_sum(self):
        self.assertEqual(large_continues_sum([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(large_continues_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        self.assertEqual(large_continues_sum([-1, 1]), 1)
        self.assertEqual(large_continues_sum([]), 0)


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))
