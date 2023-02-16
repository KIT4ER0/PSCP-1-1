"""saitama"""
def main():
    """main"""
    exer1, exer2 = int(input()), int(input())
    exer3, exer4 = int(input()), int(input())
    num1, num2 = int(input()), int(input())
    num3, num4 = int(input()), int(input())

    cal1 = exer1 / num1
    cal2 = exer2 / num2
    cal3 = exer3 / num4
    cal4 = exer4 / num3

    for _ in range(4):
        if cal1 <= cal2:
            cal1, cal2 = cal2, cal1
        if cal2 <= cal3:
            cal2, cal3 = cal3, cal2
        if cal3 <= cal4:
            cal3, cal4 = cal4, cal3
    print(int(cal1 + 0.999999999))
main()
