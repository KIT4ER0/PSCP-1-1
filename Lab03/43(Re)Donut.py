"""Donut"""
def main():
    """main"""
    price = int(input())
    number = int(input())
    free = int(input())
    need = int(input())
    to_need = need//(number+free)
    if need == 0:
        print("0 0")
    elif need > 0:
        ddd = to_need*(number+free)
        sumleft = need - ddd
        if sumleft > number:
            sumleft = number
        if sumleft >= number:
            ddd = ddd+(number+free)
        else:
            ddd = ddd+sumleft
        sumprice = (price*to_need*number) + (sumleft*price)
        print("%d %d" %(sumprice, ddd))
main()
