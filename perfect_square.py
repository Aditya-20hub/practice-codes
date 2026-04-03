def is_square(a:int) -> bool:
    """
    >>> assert is_square(25)
    >>> assert not is_square(24)
    >>> assert is_square(16)
    >>> assert is_square(9)
    >>> assert is_square(9)    
    """
    i=0    
    while i * i <= a:
        
       if i * i == a:
           return True
           
       else:
           i = i+1
    return False           
          
if __name__ == '__main__':
    print(is_square(90))    