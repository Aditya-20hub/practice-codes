def fact(num: int) -> int:
    """
    Calculate the factorial between 
    
    >>> assert fact(6) == 720
    >>> assert fact(8) == 40320
    >>> assert fact(1) == 1
    """
    retval = 1
    while num != 0:
        retval *= num
        num -= 1
    return retval


def power(num: int, p: int) -> int:
    """
    >>> assert power(2, 7) == 128
    >>> assert power(0, 2) == 0
    >>> assert power(8, 4) == 4096
    """
    retval = 1
    while p != 0:
        retval *= num
        p -= 1
    return retval


def conditional(n: int) -> None:
    i = 1
    while i <= 10:
        mul = i * n
        if i % 2 == 0:
            print(f"{mul}-even")
        else:
            print(f"{mul}-odd")
        i += 1


def combination(n: int, r: int) -> int:
    """
    calculate The combination between n and r.
    :param n: Total number of events.
    :param r: Selections.
    :return: combination between n and r.
    
    
    >>> assert combination(4, 2) == 
    >>> assert combination(5, 0) == 1
    """
    if r > n:
        return 0

    numerator = fact(n)
    denominator = fact(r) * fact(n - r)
    return numerator / denominator


def series(x: int, n: int) -> float:
    retval = 0
    i = 0
    while i < n:
        if i % 2 == 0:  
            retval = retval + power(x, i) / fact(i)
        else:
            retval = retval - power(x, i) / fact(i)
        i += 1
    return retval


if __name__ == '__main__':
    print(combination(3, 2))