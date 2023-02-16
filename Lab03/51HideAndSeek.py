"""HideAndSeek"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    while True:
        if num1 < num2:
            print(num1)
        else:
            break
        num1 += num3
main()