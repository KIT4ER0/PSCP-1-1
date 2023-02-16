"""3nPlus1"""
def main():
    """main"""
    while True:
        count = 1
        num = int(input())
        if num == 0:
            break
        while num != 1:
            if num%2 == 0:
                num /= 2
                count += 1
            else:
                num = num*3+1
                count += 1
        print(count)
main()
