"""Sequence X"""
def main():
    """main"""
    num = int(input())
    for i in range(-(num-1), num):
        for j in range(-(num-1), num):
            if num - abs(i) >= abs(j) +1:
                print("%02d" %(num-abs(j) - abs(i)), end=" ")
            else:
                print("  ", end=" ")
        print()
main()
