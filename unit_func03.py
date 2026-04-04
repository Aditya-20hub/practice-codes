from combination import fact, power, combination

def combine_sum (x:int, n:int) -> float):
    retval = 0
    i = 0
    while i < n:
        retval = retval + combination(n,n+1) * power(x,i) / fact(i)
        i += 1
    return retval
    