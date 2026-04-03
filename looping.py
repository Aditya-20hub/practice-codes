def loop_str(txt:str, num:int) -> str:
    retval = "  "
    while num > 0:
      retval = retval + txt 
      num = num - 1
    return retval

if __name__ == '__main__':
    print(loop_str("Adi", 3))    