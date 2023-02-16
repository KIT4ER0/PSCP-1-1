"""Elo"""
def main():
    """main"""
    raa = int(input())
    rbb = int(input())
    txt = input()
    eaa = 1 / (1+(10**((rbb-raa)/400)))
    ebb = 1 / (1+(10**((raa-rbb)/400)))
    if txt == "A":
        print("%.2f" %eaa)
    elif txt == "B":
        print("%.2f" %ebb)
main()
