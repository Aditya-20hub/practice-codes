from combination import fact, power, conditional, combination

def product_func(x:int) -> float:
    
    """
    calculate the producte function of x.
    
    :param x: base values.
    :return: product function of x
    """
    if x >= 4:
        return f(x-1) - f(x-2) / f(x-3)
    elif x == 3:
        return 
    elif x == 1:
        return 
    elif x == 0:
        return 3.14159
    else:
    return("Invalid Input")
    