"""SqFree"""
def sqfree(num):
    """-"""
    if num%2 == 0:
        num /= 2
    if num%2 == 0:
        return False
    for i in range(3, int(num**0.5)+1):
        if num%i == 0:
            num /= i
        if num%i == 0:
            return False
    return True

def main():
    """main"""
    num = int(input())
    ans = 0
    for i in range(1, num+1):
        if sqfree(i):
            ans += 1
    print(ans)
main()
