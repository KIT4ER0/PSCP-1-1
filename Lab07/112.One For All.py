"""One For All"""
def main():
    """main"""
    num = int(input())
    plus = 0
    ans = ""
    for _ in range(num):
        txt = input()
        plus += 1
        if plus == num:
            ans += (txt + "_%d" %num)
        elif plus%2 == 0:
            ans += (txt + "-"*plus)
        else:
            ans += (txt + "*"*plus)
    print(ans)
main()
