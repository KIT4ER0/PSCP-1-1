"""RightArrow"""
def main():
    """main"""
    lenght = int(input())
    hight = int(input())
    hight1 = (hight//2)+1
    hight2 = hight-hight1
    for i in range(hight1):
        print(" "*(i) + "*"*lenght)
    for j in range(hight2):
        print(" "*((hight2-j)-1) + "*"*lenght)
main()
