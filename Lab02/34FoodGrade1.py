"""food"""
 
def cal(num):
    """cal"""
    if 50 <= num <= 70:
        return 1
    else:
        return 0
 
def chicken_input(aaa):
    """input"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    num9 = int(input())
    num10 = int(input())
    num11 = int(input())
    num12 = int(input())
    aaa += cal(num1)
    aaa += cal(num2)
    aaa += cal(num3)
    aaa += cal(num4)
    aaa += cal(num5)
    aaa += cal(num6)
    aaa += cal(num7)
    aaa += cal(num8)
    aaa += cal(num9)
    aaa += cal(num10)
    aaa += cal(num11)
    aaa += cal(num12)
    return aaa
 
def main():
    """main"""
    total = chicken_input(0)
    total1 = chicken_input(total)
    print(total1)
main()