"""CoinChangev1"""
def main():
    """main"""
    num = int(input())
    coin25, left = divmod(num, 25)
    coin10, left = divmod(left, 10)
    coin5, coin1 = divmod(left, 5)
    print(coin25+coin10+coin5+coin1)
main()
