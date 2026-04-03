def while_loop (start:int, stop:int) -> None: 
    i = start
    while i <= stop:
        j = 1
        while j <= 10:
            print(f"{i} * {j} = {i * j}")
            j += 1
        i += 1

if __name__ == '__main__':
    while_loop(2, 8)
    