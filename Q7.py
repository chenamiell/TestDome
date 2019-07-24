def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    hash_map = {}
    for i, n in list(enumerate(numbers)):
        if target_sum - n in hash_map:
            return hash_map[target_sum - n], i
        hash_map[n] = i
    return None


print(find_two_sum([3, 1, 5, 7, 5, 9], 10))