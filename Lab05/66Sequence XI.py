"""Sequence XI"""
def main():
    """main"""
    num = int(input())
    for i in range(-num+1, num, 1):
        for j in range(-num+1, num):
            if abs(i) > abs(j):
                print("%02d" %(num-abs(i)), end=" ")
            else:
                print("%02d" %(num-abs(j)), end=" ")
        print()
main()
