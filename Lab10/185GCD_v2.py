"""GCD_v2"""
def main(num_a, num_b):
    """-"""
    gcd = 1
    while num_b != 0:
        ttt = num_b
        num_b = num_a%num_b
        num_a = ttt
    gcd = num_a
    print(gcd)
main()
