def is_triangle(a, b, c) -> bool:
    """
    >>> assert is_triangle(5, 7, 10)
    >>> assert is_triangle(2, 7, 3)
    >>> assert is_triangle(10, 50, 40)
    
    
    """
    
    if a+b>c and b+c>a and c+a>b:
        return True
    else:
        return False
 
 
def is_right_triangle(a, b, c):
    if is_triangle(a, b, c) == False:
        return False
    if a*a + b*b == c*c:
        return True
    else:
        return False
 
 
if __name__ == '__main__':
    whether_is_right_triangle = is_right_triangle(3, 2, 5)
    print(whether_is_right_triangle)