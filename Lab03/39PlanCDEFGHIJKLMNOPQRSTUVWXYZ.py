"""Plan"""
def main():
    """main"""
    text = input()
    line1 = float(input())
    line2 = float(input())
    line3 = float(input())
    if text == "Ascend":
        aaa(line1, line2, line3)
    elif text == "Descend":
        bbb(line1, line2, line3)
 
def bbb(num1, num2, num3):
    """Des"""
    if (num1 > num2 and num1 > num3 and num2 > num3) or (num1 == num2 == num3):
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    elif num1 > num2 and num1 > num3 and num3 > num2:
        print("%.2f, %.2f, %.2f" %(num1, num3, num2))
    elif num2 > num1 and num2 > num3 and num1 > num3:
        print("%.2f, %.2f, %.2f" %(num2, num1, num3))
    elif num2 > num1 and num2 > num3 and num3 > num1:
        print("%.2f, %.2f, %.2f" %(num2, num3, num1))
    elif num3 > num1 and num3 > num2 and num1 > num2:
        print("%.2f, %.2f, %.2f" %(num3, num1, num2))
    elif num3 > num1 and num3 > num2 and num2 > num1:
        print("%.2f, %.2f, %.2f" %(num3, num2, num1))
    elif num1 == num2 and num1 > num3:
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    elif num2 == num3 and num2 > num1:
        print("%.2f, %.2f, %.2f" %(num2, num3, num1))
    elif num1 == num2 and num1 < num3:
        print("%.2f, %.2f, %.2f" %(num3, num1, num2))
    elif num2 == num3 and num2 < num1:
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    elif num1 == num3 and num1 > num2:
        print("%.2f, %.2f, %.2f" %(num1, num3, num2))
    elif num1 == num3 and num1 < num2:
        print("%.2f, %.2f, %.2f" %(num2, num1, num3))
 
def aaa(num1, num2, num3):
    """Asc"""
    if (num1 < num2 and num1 < num3 and num2 < num3) or (num1 == num2 == num3):
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    elif num1 < num2 and num1 < num3 and num3 < num2:
        print("%.2f, %.2f, %.2f" %(num1, num3, num2))
    elif num2 < num1 and num2 < num3 and num1 < num3:
        print("%.2f, %.2f, %.2f" %(num2, num1, num3))
    elif num2 < num1 and num2 < num3 and num3 < num1:
        print("%.2f, %.2f, %.2f" %(num2, num3, num1))
    elif num3 < num1 and num3 < num2 and num1 < num2:
        print("%.2f, %.2f, %.2f" %(num3, num1, num2))
    elif num3 < num1 and num3 < num2 and num2 < num1:
        print("%.2f, %.2f, %.2f" %(num3, num2, num1))
    elif num1 == num2 and num1 < num3:
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    elif num2 == num3 and num2 < num1:
        print("%.2f, %.2f, %.2f" %(num2, num3, num1))
    elif num1 == num2 and num1 > num3:
        print("%.2f, %.2f, %.2f" %(num3, num1, num2))
    elif num2 == num3 and num2 > num1:
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    elif num1 == num3 and num1 < num2:
        print("%.2f, %.2f, %.2f" %(num1, num3, num2))
    elif num1 == num3 and num1 > num2:
        print("%.2f, %.2f, %.2f" %(num2, num1, num3))
main()