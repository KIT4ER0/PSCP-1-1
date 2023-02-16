"""milk"""
def main():
    """main"""
    price = int(input())
    pro = int(input())
    free = int(input())
    money = int(input())
    num_bot = money//price
    num_fa = num_bot
    while num_fa >= pro and pro > 0:
        temp1 = (num_fa//pro)*free
        temp2 = num_fa%pro
        num_bot += temp1
        num_fa = temp1+temp2
    print(num_bot)
main()
