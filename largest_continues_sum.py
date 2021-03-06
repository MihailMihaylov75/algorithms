__author__ = 'Mihail Mihaylov'


def large_continues_sum(arr):
    if not len(arr):
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum
