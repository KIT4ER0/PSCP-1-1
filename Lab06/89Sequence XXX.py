"""Sequence XXX"""
def main():
    """main"""
    height = int(input())
    number = int(input())
    for i in range(1, height+1):
        line = ""
        for j in range(1, height+1):
            if i == 1 or i == height or j == 1 or j == height or i == j or j == height-i+1:
                line += "*"
            else:
                line += " "
        print(((line+" ")*number))
main()
