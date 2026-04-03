def greater_value(a, b, c) -> str:
 
    """ 
 
    Returns which value is greatest.

    >>> greater_value(4, 7, 8)
    'c is greater than a and b'
    
     >>> greater_value(9, 6, 7)
    'c is greater than a and b'
    
     >>> greater_value(8, 3, 6)
    'c is greater than a and b'
    
    """
     
    
    
   
    if a > b and a > c:
        return " a is greater than b and c"
    elif b > a and  b > c:
        return "b is greater than a and c"
    elif c > a and c > b:
        return "c is greater than a and b"
    elif a == b and b > c and a > c: 
        return "a and b are greater than c"
    elif a == c and a > b and c > b:
        return "a and c are greater than b"
    elif b == c and b > a and c > a:
        return "b and c are greater than a"
            
    else:
        return "a, b and c are all equal"
        
        
if __name__ == '__main__':
    print(greater_value(25, 20, 25))
      