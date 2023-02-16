"""Sequence III"""
def main():
    """main"""
    num = int(input())
    for i in range(0, num):
        for j in range(num):
            print(2+i+j, end=" ")
        print()
main()