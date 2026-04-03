def is_even(a: int) -> bool:
    """
    >>> assert not is_even(5)
    
    >>> assert not is_even(7)
    
    >>> assert is_even(0)
    
    >>> assert not is_even(5)
    
    >>> assert is_even(4)
    """
    if a % 2 == 0:
        return True
    else:
        return False
        
if __name__ == '__main__':
    whether_is_even = is_even(10)
    print(whether_is_even)
