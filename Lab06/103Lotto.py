"""Lotto"""
def main():
    """main"""
    one = input()
    two = input()
    threef1 = input()
    threef2 = input()
    threeb1 = input()
    threeb2 = input()
    buy = input()
    money = 0
    if buy == one == buy:
        money += 6000000
    if buy[4:6] == two:
        money += 2000
    if buy[0:3] == threef1:
        money += 4000
    if buy[0:3] == threef2:
        money += 4000
    if buy[3:6] == threeb1:
        money += 4000
    if buy[3:6] == threeb2:
        money += 4000
    if int(one) == 0 and (int(buy) == 999999 or int(buy) == 1):
        money += 100000
    elif int(one) == 999999 and (int(buy) == 0 or int(buy) == 999998):
        money += 100000
    elif (int(buy)) == int(one)+1 or (int(buy)) == int(one)-1:
        money += 100000
    print(money)
main()
