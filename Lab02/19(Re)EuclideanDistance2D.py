"""EuclideanDistance2D"""
import math
def main():
    """main"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    print(math.sqrt((num1-num3)**2 + (num2-num4)**2))
main()