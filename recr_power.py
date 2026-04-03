def power(num:int, p:int) -> int:
    
    """
    >>> assert power(3, 4) == 81
    >>> assert power(8, 7) == 2097152
    >>> assert power(7, 2)== 49 
    
    """
    if p == 0:
        return 1
    else:    
        return num * power(num, p - 1)


if __name__ == '__main__':
    print(power(3, 4))