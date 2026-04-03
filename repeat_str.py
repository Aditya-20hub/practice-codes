def repeat_str(txt:str, num:int) -> str:
    if num <= 0:
        return "  "
    elif num == 1:
        return txt
    
    else:
        return txt + repeat_str(txt, num-1)

if __name__ == '__main__':
    print(repeat_str("Adi", 5))