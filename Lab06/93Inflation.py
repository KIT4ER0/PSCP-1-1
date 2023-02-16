"""Inflation"""
def main():
    """main"""
    price = float(input())
    year = int(input())
    for i in range(year):
        new_price = price*0.0381
        price = new_price
    print()