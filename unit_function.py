from combination import fact, power, combination
from even_or_odd import is_even 
import math

def unit_func02(x: int) -> float:
    """
    calculate the unit function of x.
    
    :param x: base values.
    :return: product function of x
    """
    if x >= 4:
        return (unit_func02(x-1) - unit_func02(x-2)) / unit_func02(x-3) 
    elif x == 3 or x == 2:
        return math.sqrt(x)
    elif x == 1:
        return math.e
    elif x == 0:
        return math.pi
    else:
        return ("Invalid Input")
    
    
def product_func(n: int) -> float:
    """
    calculate the product function of n.
    
    :param n: number of terms.
    :return: product function of n.
    """
    retval = 1
    i = 0 
    while i < n:
        if is_even(i):
            retval = retval * unit_func02(i)
        else:
            retval = retval *(-unit_func02(i))
        i += 1
    return retval

  
if __name__ == '__main__':
    print(product_func(7))
    