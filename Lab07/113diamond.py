"""diamond"""
def main(num):
    """main"""
    half = num//2
    for i in range(num):
        for j in range(num):
            if i == half or i+j == half or j-i == half or i-j == half or j == num-i+half-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main(int(input()))