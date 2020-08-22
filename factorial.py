__author__ = 'Mihail Mihaylov'
import sys
import unittest


def fact(n):
    """"Recursive factorial"""
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


def fact_non_recursive(n):
    """"Non recursive factorial"""
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        while n > 1:
            factorial *= n
            n -= 1
        return factorial


class TestFactorial(unittest.TestCase):
    """"Class to factorial algorithm"""
    def test_factorial_recursive(self):
        """"Test recursive factorial"""
        self.assertEqual(fact(10), 3628800)
        self.assertEqual(fact(5), 120)
        self.assertEqual(fact(0), 1)

    def test_factorial_non_recursive(self):
        """"Test non recursive factorial"""
        self.assertEqual(fact_non_recursive(10), 3628800)
        self.assertEqual(fact_non_recursive(5), 120)
        self.assertEqual(fact_non_recursive(0), 1)


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2, stream=sys.stdout))