"""Ball"""
def main():
    """main"""
    txt = input()
    tot = 1
    for i in txt:
        if i == "A" and tot == 2:
            tot = 1
        elif i == "A" and tot == 1:
            tot = 2
        if i == "B" and tot == 3:
            tot = 2
        elif i == "B" and tot == 2:
            tot = 3
        if i == "C" and tot == 1:
            tot = 3
        elif i == "C" and tot == 3:
            tot = 1
    print(tot)
main()
