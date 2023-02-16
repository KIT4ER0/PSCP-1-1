"""MissingNumber"""
def main():
    """main"""
    num = []
    check = []
    num_in = int(input())
    for i in range(num_in+1):
        check.append(i)
    for _ in range(num_in):
        num_in2 = int(input())
        num.append(num_in2)
        if num_in2 == 0:
            break
    num.sort()
    for i in num:
        check.remove(i)
    for i in check:
        print(i)
main()
