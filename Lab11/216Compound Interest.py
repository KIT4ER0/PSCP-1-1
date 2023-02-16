'''Compound Interest'''
def main():
    '''_'''
    money = int(input())
    rrr = float(input())
    year = int(input())
    for _ in range(1, year + 1):
        rate = money*rrr/100
        money += rate
    print("%.2f" %money)
main()
