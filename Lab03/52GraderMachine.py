"""GraderMachine"""
def main():
    """main"""
    num1 = int(input())
    num2 = int(input())
    ans = 0
    print("pass :", end=" ")
    if num1 < num2:
        for i in range(num1, num2+1, 1):
            if i%2 == 0:
                ans += i
                print("%d" %i, end=" ")
    else:
        for i in range(num1, num2-1, -1):
            if i%2 == 0:
                ans += i
                print("%d" %i, end=" ")
    print()
    print("Sum : %d" %ans)
main()