"""isprime_small"""
def main(num, result):
    """main"""
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                result = False
    else:
        result = False
    if result:
        print("Yes")
    else:
        print("No")
main(int(input()), True)
