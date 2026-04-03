def febo(x:int) -> int:
    """
    >>> assert febo(3) == 2
    >>> assert febo(2) == 1
    >>> assert febo(5) == 5
    
    """
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return febo(x - 1) + febo(x - 2)  
        
        
if __name__ == '__main__':    
    print(febo(3))        