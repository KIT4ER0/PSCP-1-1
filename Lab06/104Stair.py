"""Stair"""
def main():
    """main"""
    cat = True
    check = 0
    sum1 = 0
    highest = int(input())
    floor = int(input())
    for _ in range(1, floor + 1):
        jumping = int(input())
        check = check + jumping
        if jumping > highest:
            cat = False
        elif check == highest:
            sum1 = sum1 + 1
            check = 0
        elif check > highest:
            sum1 = sum1 + 1
            check = jumping
    if check > 0:
        sum1 = sum1 + 1
    if cat:
        print("%d" % sum1)
    else:
        print("NO")
main()
