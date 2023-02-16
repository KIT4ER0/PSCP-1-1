"""Sequence IV"""
def main():
    """main"""
    num = int(input())
    aaa = 1
    for i in range(aaa, num+1):
        for i in range(aaa, num+1):
            print(i, end=" ")
            aaa += 1
            num += 1
        print()
    aaa += 1
main()