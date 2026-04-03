from unit_func import unit_func
       
def sum_unit_func(x: int, n: int) -> float:
    """
    Calculate sum_unit_func of x and n.
    
    :param x: Base value.
    :param n: number of terms.
    :return: sum_unit_func of x and n
    """
    retval = 0
    i = 0
    while i < n:
        retval = retval + unit_func(x, i, n)
        i += 1
    return retval    
    

if __name__ == "__main__":
        print(sum_unit_func(3, 4))
