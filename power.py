def power(num:int, p:int) -> int:
    
    """
    >>> assert power(2, 7) == 128
    >>> assert power(0, 2) == 0
    >>> assert power(8, 4) == 4096
    
    """
    
    retval = 1
    while p != 0:
        retval = num * retval
        p -= 1
    return retval    
    
    
if __name__ == '__main__':
        print(power(3, 3))