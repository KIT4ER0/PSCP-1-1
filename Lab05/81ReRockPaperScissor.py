"""RPS"""
def main():
    """main"""
    txt = input()
    aaa = 0
    bbb = 0
    for i in range(0, len(txt), 2):
        result = (txt[i] + txt[i+1])
        if result == "RP" or result == "PS" or result == "SR":
            bbb += 1
        elif result == "PR" or result == "SP" or result == "RS":
            aaa += 1
    if aaa > bbb:
        print("A win", str(aaa)+"-"+str(bbb))
    elif bbb > aaa:
        print("B win", str(bbb)+"-"+str(aaa))
    else:
        print("DRAW", str(aaa))
main()
