def conditional(n: int) -> int:
    i = 1
    while i <= 10:
        mul = i * n
        if i % 2 == 0:
            print(f"{mul}-even")
        else:
            print(f"{mul}-odd")
        i += 1


if __name__ == '__main__':
    conditional(2)
    
    
    
    
    


