__author__ = 'Mihail Mihaylov'


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
