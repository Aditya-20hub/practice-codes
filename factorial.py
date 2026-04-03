def factorial(num:int) -> int:
    """
    >>> assert factorial(6) == 720
    >>> assert factorial(8) == 40320
    >>> assert factorial(1) == 1
    
    """
    retval = 1
    while num!=0:
        retval= retval * num
        num -=1 
    return retval
    
    
if __name__ == '__main__':    
    print(factorial(6))
   
        
        
        
        
        
        
        
        
        
        
        
