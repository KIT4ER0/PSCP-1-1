"""Triangle"""
def main():
    """main"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num3+0.01 >= ((num1**2 + num2**2)**0.5) and num3-0.01 <= ((num1**2 + num2**2)**0.5):
        print("Yes")
    elif num2+0.01 >= ((num1**2 + num3**2)**0.5) and num2-0.01 <= ((num1**2 + num3**2)**0.5):
        print("Yes")
    elif num1+0.01 >= ((num2**2 + num3**2)**0.5) and num1-0.01 <= ((num2**2 + num3**2)**0.5):
        print("Yes")
    else:
        print("No")
main()