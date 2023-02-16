"""ChristmasTree"""
def main():
    """main"""
    size_chrismas = int(input())
    size_tree = int(input())
    for i in range(1, size_chrismas+1):
        print(" "*(size_chrismas-i), end="")
        print("*"*(i*2-1))
    for _ in range(size_tree):
        print(" "*(size_chrismas-2), end="")
        print("---")
main()
