def unit_func02(x: int) -> float:
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
   
   

if __name__ == '__main__':
    print(product_func(7))
    