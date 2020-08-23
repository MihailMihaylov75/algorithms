__author__ = 'Mihail Mihaylov'


def fibonacci_generator():
    """"Fibonacci generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_with_generator(n):
    """"Get fibonacci nums with generator"""
    f = fibonacci_generator()
    fib_nums = []
    for i in range(n):
        fib_nums.append(next(f))
    return fib_nums


def fib_recursive(n):
    """"Find fibonacci nums recursive"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_recursive2(n):
    """"Find fibonacci nums recursive vol 2"""
    return 0 if n == 0 else 1 if n == 1 else fib_recursive(n-1) + fib_recursive(n-2)


def get_fibonacci(func, n):
    """"Get fibonacci nums"""
    fib_nums = []
    for i in range(n):
        fib_nums.append(func(i))
    return fib_nums
