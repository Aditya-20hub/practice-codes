def is_quad(a, b, c, d) -> bool:
    """
    >>> assert is_quad(3, 6, 7, 2)
    >>> assert is_quad(5, 5, 8, 2)
    >>> assert is_quad(0, 8, 6, 4)
    >>> assert is_quad(23, 90, 75, 24)
    >>> assert is_quad(37, 65, 73, 27)
 
    
    """
    if a + b + c <= d:
        return False
    elif a + b + d <= c:
        return False
    elif a + c + d <= b:
        return False
    elif b + c + d <= a:
        return False
    else:
        return True
 


def is_parellelogram(a, b, c, d) -> bool:
    """
    
    >>> assert is_parellelogram(3, 2, 3, 2)
    >>> assert is_parellelogram(7, 6, 9, 4)
    >>> assert is_parellelogram(3, 2, 3, 2)
    >>> assert is_parellelogram(3, 2, 3, 2)

   
    """
    if is_quad(a, b, c, d)== False:
        return False 
    if  a != c:
        return False
    elif b != d:
        return False
    else:
        return True

  
             
             
        
  
def is_rectangle(a, b, c, d) -> bool:
    """
       >>> assert is_rectangle(2, 4, 5, 7)
       >>> assert is_rectangle(2, 2, 2, 2)
       >>> assert is_rectangle(6, 8, 9, 2)
       >>> assert is_rectangle(9, 2, 4, 6)

    """    
    if is_parellelogram(a, b, c, d) == False: 
          return False
    if a*a + b*b == c*c:
          return False
    else:
          return True
          
 
     
     

def is_square(a, b, c, d) -> bool:
    """
       >>> assert is_square(9, 9, 9, 9)
       >>> assert is_square(7, 7, 7, 6)
       >>> assert is_square(4, 4, 4, 4)
       >>> assert is_square(7, 6, 1, 3)
    
    
    """
    if is_rectangle(a, b, c, d) == False:
          return False
    if  a != b:
          return False
    elif b != c:
          return False
    else:
        return True

if __name__ == '__main__':
     print(is_rectangle(4, 5, 6, 8))         
         
         