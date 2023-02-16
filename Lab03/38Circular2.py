"""Circular II"""
import math
def main():
    """main"""
    line1 = float(input())
    line2 = float(input())
    line3 = float(input())
    line4 = float(input())
    line5 = float(input())
    line6 = float(input())
    ddd = math.sqrt((line1-line4)**2 + (line2-line5)**2)
    sumr = (line3+line6)
    if ddd < sumr:
        print("Yes")
    else:
        print("No")
main()