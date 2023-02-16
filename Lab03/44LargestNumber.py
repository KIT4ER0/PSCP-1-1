"""LargestNumber"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    last = str(num1) + str(num2) + str(num3)
    last = compare((str(num1) + str(num3) + str(num2)), last)
    last = compare((str(num2) + str(num1) + str(num3)), last)
    last = compare((str(num2) + str(num3) + str(num1)), last)
    last = compare((str(num3) + str(num1) + str(num2)), last)
    last = compare((str(num3) + str(num2) + str(num1)), last)
    print(int(last))

def compare(aaa, bbb):
    """compare"""
    if aaa > bbb:
        return aaa
    return bbb
main()
