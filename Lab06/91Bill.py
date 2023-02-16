"""Bil"""
def main():
    """main"""
    num = int(input())
    fees = num*0.1
    if fees > 1000:
        fees = 1000
        num = num + fees
        num = num + num*0.07
        print("%.2f" %num)
    elif fees < 50:
        fees = 50
        num = num + fees
        num = num + num*0.07
        print("%.2f" %num)
    else:
        num = num + fees
        num = num + num*0.07
        print("%.2f" %num)
main()
