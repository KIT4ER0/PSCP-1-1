"""SumOfNumber"""
def main():
    """main"""
    ans = int(input())
    total = 0
    while True:
        num = int(input())
        if num == -1:
            break
        total += num
        if total == ans:
            break
    print(total)
main()