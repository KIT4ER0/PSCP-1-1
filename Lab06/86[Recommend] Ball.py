"""Ball"""
def main():
    """main"""
    num = float(input())
    num = num*0.6
    count = 0
    while True:
        if num >= 0.01:
            num = num*0.6
            count += 1
        else:
            break
    print(count)
main()
