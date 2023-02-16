"""RES"""
def main():
    """main"""
    price = float(input())
    to_price = float(input())
    discount = float(input())
    price_plus = float(input())
    if price+price_plus >= to_price:
        pay_plus = (price+price_plus)*(100-discount)/100
    else:
        pay_plus = price+price_plus

    if price >= to_price:
        pay_noplus = price*(100-discount)/100
    else:
        pay_noplus = price

    ans = abs(pay_plus - pay_noplus)
    if pay_plus < pay_noplus:
        print("Yes %.3f" %ans)
    elif pay_plus > pay_noplus:
        print("No %.3f" %ans)
    else:
        print("Yes")
main()
