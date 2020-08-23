__author__ = 'Mihail Mihaylov'


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
