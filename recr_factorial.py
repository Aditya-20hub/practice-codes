def recr_factorial(num: int) -> int:
    """
    >>> assert recr_factorial (0) == 1
    >>> assert recr_factorial (5) == 120
    >>> assert recr_factorial (1) == 2
    
    """
    if num == 0:
        return 1
    return num * recr_factorial(num - 1)
   
     
     
def power(num:int, p:int) -> int:
    
    """
    >>> assert power(3, 4)
    >>> assert power(8, 7)
    >>> assert power(9, 2)
    
    """
    
    if p == 0:
        return 1
    else:    
        return num * power(num, p - 1)



    