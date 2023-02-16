"""CoPrimeV1"""
def main(num1, num2, gcd):
    """-"""
    while num2 != 0:
        ttt = num2
        num2 = num1%num2
        num1 = ttt
    gcd = num1
    if gcd == 1:
        print("YES", gcd, sep="\n")
    else:
        print("NO", gcd, sep="\n")
main(int(input()), int(input()), 1)
