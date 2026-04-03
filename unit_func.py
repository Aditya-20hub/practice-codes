from combination import power, fact, combination

def is_divisible_by_n(num: int, n: int) -> bool:
    if num % n == 0 :
        return True
    else: 
        return False
        

def unit_func(x: int, i: int, n:int) -> float:
    """
    Calculate the unit_func of x, i  and n.
    
    :param x: base value.
    :param i: ittration value.
    :param n: number of terms.
    :return: unit_func of x, i and n.
    """
    if is_divisible_by_n(i,5):
        return power(x, combination(n, i)) / fact(i-2)
        
    elif is_divisible_by_n(i, 3):
        return combination(n, i) * power(x, i) / fact(i-3)
    
    elif is_divisible_by_n(i, 2):
        return power(x, i) / fact (i)
        
    elif i == 0:
        return power(x, 0) / fact(0)
    
    else:
        return (n-1) * (-power(x, i)) / fact(i)


if __name__ == "__main__":
        print(unit_func(5, 8, 3))
