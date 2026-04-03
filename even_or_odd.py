def even_or_odd(a:int) -> bool:
    """
    >>> assert even_or_odd(5) == 'odd'
    
    >>> assert even_or_odd(7) == 'even'
    
    >>> assert even_or_odd(0) == 'odd'
    
    >>> assert even_or_odd(5) == 'odd'
    
    >>> assert even_or_odd(4) == 'even'
    
    
    """
    if a % 2 == 0:
        return "even"
    else:
        return "odd"
        
if __name__ == '__main__':
    whether_even_or_odd = even_or_odd (10)
    print(whether_even_or_odd)
    