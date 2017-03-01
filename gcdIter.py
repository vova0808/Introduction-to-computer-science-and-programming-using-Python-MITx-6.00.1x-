def gcdIter(a, b):
    """
    a, b : positive integers

    returns: a positive integer, the greatest common divisor of a & b
    """

    common_divisor = 1
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            if i > common_divisor:
                common_divisor = i
    return common_divisor
