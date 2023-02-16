"""Sequence V"""
def main():
    """main"""
    num = int(input())
    for _ in range(num):
        for _ in range(0, 7):
            if num > 0:
                print(num, end=" ")
                num -= 1
        print()
main()