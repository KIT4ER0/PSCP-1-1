"""data"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    ans1 = comparex(num1, num2)
    ans2 = comparex(ans1, num3)
    ans3 = comparex(ans2, num4)
    ans4 = comparex(ans3, num5)
    ans5 = comparex(ans4, num6)
    ans6 = comparex(ans5, num7)
    total = comparex(ans6, num8)
    print(total)
 
def comparex(xxx, yyy):
    """comparex"""
    if xxx > yyy:
        return xxx
    else:
        return yyy
main()