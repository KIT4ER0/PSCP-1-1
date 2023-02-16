"""TupleSad"""
def main():
    """Tuple"""
    txt = input().split()
    txt2 = input()
    length = txt.count(txt2)
    num = txt.index(txt2)
    for _ in range(length):
        for _ in range(length):
            print(num, end=" ")
        print()
main()
