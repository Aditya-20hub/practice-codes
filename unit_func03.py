from combination import fact, power, combination

def combine_sum (x:int, n:int) -> float:
    """
    calculate 1combine_sum of x and n.
    
    :param x: base value.
    :param n: number of terms.
    :return: cumbine_sum of x and n.
    """
    retval = 0
    i = 0
    while i < n:
        retval = retval + combination(n,n) * power(x,i) / fact(i)
        i += 1
    return retval
    
  
  
if __name__ == "__main__":
        print(combine_sum(5, 8))  