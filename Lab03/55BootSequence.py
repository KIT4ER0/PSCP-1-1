"""BootSequence"""
def main():
    """main"""
    num = int(input())
    aaa = 1
    while True:
        if aaa < num:
            print(str(aaa) +"_", end="")
        elif aaa == num:
            print(aaa)
        else:
            break
        aaa += 1
main()