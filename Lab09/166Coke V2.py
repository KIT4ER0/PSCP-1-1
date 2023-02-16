"""Coke V2"""
def main():
    """main"""
    cost = int(input())
    pro = int(input())
    spa_cost = int(input())
    amount = int(input())
    if pro == 0:
        print(cost*amount)
        return
    if amount == 0:
        print(0)
        return
    many = amount-1
    loop_count = many//pro
    many_left = many%pro
    price2loop = (cost*(pro-1))+spa_cost
    total = cost+(loop_count*price2loop)+(many_left*cost)
    print(total)
main()
