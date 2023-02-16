"""Table I"""
def main():
    """main"""
    num = int(input())
    i = 1
    while True:
        if i < num+1:
            print("15 x " + str(i) + " = " + str(15*i))
            i += 1
        else:
            break
main()
