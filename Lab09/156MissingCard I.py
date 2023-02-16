"""MissingCard I"""
def main():
    """main"""
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    allcard = []
    for i in rank:
        allcard.append(i+"S")
        allcard.append(i+"H")
        allcard.append(i+"D")
        allcard.append(i+"C")
    for _ in range(51):
        misscard = input()
        if misscard in allcard:
            allcard.remove(misscard)
    print(*allcard)
main()
