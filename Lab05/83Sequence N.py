"""Sequence N"""
def main():
    """main"""
    num = int(input())
    for i in range(num):
        for j in range(num):
            if j == 0 or j == num-1 or (i == j and (j > 0 and j < num-1)):
                print("*", end="")
            else:
                print(end=" ")
        print()
main()

