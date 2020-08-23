__author__ = 'Mihail Mihaylov'


def balance_parentheses_check(s):
    if len(s) % 2 != 0:
        return False

    opening_brackets = set('{([')
    matches = set([('(', ')'), ('{', '}'), ('[', ']')])
    stack = []

    for bracket in s:
        if bracket in opening_brackets:
            stack.append(bracket)
        else:
            if not stack:
                return False
            last_opened = stack.pop()
            if (last_opened, bracket) not in matches:
                return False

    return len(stack) == 0
