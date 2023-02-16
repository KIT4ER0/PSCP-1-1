"""print"""
def main():
    """print"""
    num1 = int(input())
    num2 = float(input())
    num3 = input()
    text1 = "%30d" %num1
    text2 = "%030d" %num1
    text3 = "%0.2f" %num2
    text4 = "%0.12f" %num2
    text5 = "%40s" %num3
    print(text1)
    print(text2)
    print(text3)
    print(text4)
    print(text5)
 
main()