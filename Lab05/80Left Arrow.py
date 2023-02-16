"""Left Arrow"""
def main():
    """main"""
    lenght = int(input())
    hight = int(input())
    hight1 = (hight//2)+1
    hight2 = hight-hight1
    for i in range(hight1):
        print(" "*((hight1-i)-1)+"*"*lenght)
    for j in range(hight2):
        print(" "*(j+1)+"*"*lenght)
main()
