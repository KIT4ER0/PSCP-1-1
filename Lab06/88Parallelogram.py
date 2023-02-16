"""Parallelogram"""
def main():
    """main"""
    txt = input()
    for i in range(0, len(txt)+1):
        if i == 0:
            continue
        elif i != len(txt):
            print(" ", end="")
        print(" "*(len(txt)-i-1) + txt[0:i:+1])
    for i in range(0, len(txt)+1):
        if txt[i+1:len(txt):] == "":
            continue
        print(""+txt[i+1:len(txt):]+"")
main()
