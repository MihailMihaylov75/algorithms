__author__ = 'Mihail Mihaylov'
import sys
import unittest


def pair_sum(arr, k):
    """Count pairs with given sum"""
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for val in arr:
        target = k - val
        if target not in seen:
            seen.add(val)
        else:
            output.add((min(val, target), max(val, target)))
    return ''.join(map(str, list(output)))


class TestPairSum(unittest.TestCase):
    """"Class to test pair sum"""
    def test_pair_sum(self):
        self.assertEquals(pair_sum([1, 2, 3, 4], 4), '(1, 3)')
        self.assertEquals(pair_sum([1, 3, 2, 2], 4), '(1, 3)(2, 2)')
        self.assertEquals(pair_sum([1, 2, 4, 6, 7], 50), '')
        self.assertEquals(pair_sum([], 50), '')


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))
