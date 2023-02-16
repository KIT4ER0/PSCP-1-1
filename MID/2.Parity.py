"""Parity"""
def main():
    """main"""
    txt = input()
    what = input()
    total = 0
    for i in txt:
        if i == "1":
            total += 1
    if what == "Even" and total%2 == 0:
        print(txt + "0")
    elif what == "Even" and total%2 != 0:
        print(txt + "1")
    elif what == "Odd" and total%2 == 0:
        print(txt + "1")
    elif what == "Odd" and total%2 != 0:
        print(txt + "0")
main()
