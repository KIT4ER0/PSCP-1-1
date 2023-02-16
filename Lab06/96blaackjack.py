""" Blackjack """
def main():
    """Blackjack """
    call = int(input())
    my_list = []
    for _ in range(call):
        hit = input().upper()
        my_list.append(hit)
    total = 0
    for i in my_list:
        if i == "J" or i == "Q" or i == "K":
            total += 10
        elif i == "A":
            total += 11
            if total > 21:
                total -= 10
        else:
            total += int(i)
    if total > 21 and "A" in my_list:
        total -= 10
    print(total)
main()
