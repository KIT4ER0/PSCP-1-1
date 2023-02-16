"""Align"""
import math
def main():
    """main"""
    size = int(input())
    near = input()
    txt = input()
    if near == "left":
        print(txt + " "*cal(size, txt))
    elif near == "right":
        print(" "*cal(size, txt) + txt)
    elif near == "center":
        left = math.ceil(cal(size, txt)/2)
        right = math.floor(cal(size, txt)/2)
        print(" "*left + txt + " "*right)

def cal(size, txt):
    """cal"""
    lenght = size-len(txt)
    return lenght
main()
