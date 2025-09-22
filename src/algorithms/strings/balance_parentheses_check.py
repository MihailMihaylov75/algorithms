"""
Problem:
Given a string containing only the characters '(', ')', '{', '}', '[' and ']',
determine if the input string has balanced parentheses.

A string is considered balanced if:
- Every opening bracket has a corresponding closing bracket of the same type.
- Brackets close in the correct order.

Examples:
    balance_parentheses("()") -> True
    balance_parentheses("()[]{}") -> True
    balance_parentheses("(]") -> False
    balance_parentheses("([)]") -> False
    balance_parentheses("{[]}") -> True

Constraints:
- Input string may be empty (which is considered balanced).
- Only the six bracket characters are relevant; other characters are not expected.
"""


def balance_parentheses(s: str) -> bool:
    """
    Checks whether a given string has balanced parentheses.

    :param s: String consisting of parentheses characters '()[]{}'.
    :return: True if the string is balanced, False otherwise.

    Time Complexity: O(n), where n = len(s).
    Space Complexity: O(n), for the stack of opening brackets.
    """
    if len(s) % 2 != 0:
        return False

    opening_brackets = {"{", "(", "["}
    matches = {("(", ")"), ("{", "}"), ("[", "]")}
    stack: list[str] = []

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
