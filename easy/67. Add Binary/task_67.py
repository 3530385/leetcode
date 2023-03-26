def add_binary(a:str, b:str)->str:
    return str(bin(int(a,2)+int(b,2)))[2:]

if __name__ == "__main__":
    add_binary()
