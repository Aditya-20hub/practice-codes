from combination import power
from even_or_odd import is_even


def unit_func04(x: int, n: int) -> float:
    """
    calculate unit func04 of x and n.
    
    :param x: base value:
    :param n: number of terms.
    :return: unit func of x and n.
    """
    if x <= n/2:
        return power(x, n)
    elif x > n/2:
        return power(n, x)
    elif x == 0 or n == 0:
        return 1
    else:
        return("incorrect values")



def func_div_sum(x: int, n: int) -> float:
    """
    calculate func_div_sum of x and n.
    
    :param x: base value
    :param n: number of terms.
    :return; func_div_sum of x and n.
    """    
    retval = 0 
    i = 0 
    while i < n:
        if is_even(i):
            retval = retval + unit_func04(i, n) / unit_func04(i+1, n)
        else:
            retval = retval - unit_func04(i, n) / unit_func04(i+1, n)
        i += 1
    return retval


if __name__ == '__main__':
        print(func_div_sum(2, 5))