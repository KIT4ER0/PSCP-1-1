"""Olympic"""
def coin(num):
    """coin"""
    return int(num[1]), int(num[2]), int(num[3])

def main():
    """main"""
    num_country = int(input())
    val = []
    old = ""
    count = 1
    for _ in range(num_country):
        val.append(input().split())
    val.sort()
    val.sort(key=coin, reverse=True)
    for i in range(num_country):
        if coin(val[i]) != old:
            count = i+1
        print(count, " ".join(val[i]), sum(coin(val[i])))
        old = coin(val[i])
main()
