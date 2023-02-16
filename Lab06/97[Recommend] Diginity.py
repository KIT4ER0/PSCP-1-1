"""Diginity"""
def cal(id_card):
    """cal"""
    total = 0
    for i in id_card:
        total += int(i)
    if len(str(total)) != 1:
        total = cal(str(total))
    return total

def main():
    """main"""
    while True:
        id_card = input()
        total = 0
        if id_card == "0":
            break
        else:
            total = cal(id_card)
            print(total)
main()
