"""Sequence VIII"""
def main():
    """main"""
    num = int(input())
    for i in range(1, num+1):
        for _ in range(num-i):
            print("  ", end=" ")
        for k in range(1, i+1):
            print("%02d" %k, end=" ")
        print()
main()