"""point"""
from math import sqrt
def main():
    """main"""
    num_x = float(input())
    num_y = float(input())
    num_r = float(input())
    num_xn = float(input())
    num_yn = float(input())
    aaa = sqrt((num_xn-num_x)**2 + (num_yn-num_y)**2)
    if aaa <= num_r:
        print(True)
    else:
        print(False)
main()