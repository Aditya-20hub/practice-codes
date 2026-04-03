def recr_factorial(num: int) -> int:
    """
    >>> assert recr_factorial(0) == 1
    >>> assert recr_factorial(5) == 120
    >>> assert recr_factorial(1) == 1
    
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
        


def exponential(x: int, n: int) -> float:
    """
    Calculate the values of e^x till n terms.
    
    Examples:
    
    >>> assert exponential(2, 3) == 8
    >>> assert exponential(5, 2) == 25
    >>> assert exponential(7, 0) == 1
    
    :param x: base of e^x.
    :param n: number of terms to calculate.
    :returns: value of e^x till n terms   
    """
    retval = 0   
    for i in range(n):
        retval = retval + (power(x, i) / recr_factorial(i))
    return retval    

    
if __name__ == '__main__':
    e = exponential(6, 20)    
    print(e)
