"""Shorten"""
def main(num1, result):
    """main"""
    while num1 != -1:
        num2 = int(input())
        if num1 == -1:
            break
        elif num1+1 == num2:
            first = num1
            last = num2
            while num1+1 == last:
                num1 = last
                last = int(input())
            result += ("%d-%d"%(first, num1))
            num1 = last
        else:
            result += ("%d"%num1)
            num1 = num2
        if num1 != -1:
            result += ", "
    print(result)
main(int(input()), "")
