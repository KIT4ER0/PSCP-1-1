"""Coke"""
def main(price, cover, new, want):
    """main"""
    cost, caps = price, 0
    balance = 0
    while want > 0:
        caps += 1
        balance += cost
        cost = price
        if cover == 0:
            balance = price*want
            break
        if caps == cover:
            cost = new
            caps = 0
        want -= 1
    print(balance)
main(int(input()), int(input()), int(input()), int(input()))
