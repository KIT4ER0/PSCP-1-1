"""Stepper II"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    if num1 < num2:
        for aaa in range(num1, num2+1, 1):
            print(aaa)
    elif num1 >= num2:
        for bbb in range(num1, num2-1, -1):
            print(bbb)
main()