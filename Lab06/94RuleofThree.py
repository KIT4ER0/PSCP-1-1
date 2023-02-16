"""RuleofThree"""
def main():
    """main"""
    number_all = int(input())
    for _ in range(number_all):
        price = float(input())
        weight = float(input())
        less = 0
        ans = weight/price
        if ans > less:
            less = ans
            cal(price, weight)
        else:
            less = less

def cal(price, weight):
    """cal"""
    print("%.2f %.2f" %(price, weight))
main()
