"""GCD_N"""
def cal(num_a, num_b):
    """-"""
    gcd = 1
    while num_b != 0:
        ttt = num_b
        num_b = num_a%num_b
        num_a = ttt
    gcd = num_a
    return gcd

def main():
    """main"""
    total = int(input())
    num = []
    for _ in range(total):
        num.append(int(input()))
        if len(num) == 2:
            num.append(cal(num[0], num[1]))
            num.pop(0)
            num.pop(0)
    print(*num)
main()
