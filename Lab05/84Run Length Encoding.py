"""Run Length Encoding"""
def main():
    """main"""
    txt = input()
    count = 0
    val = ""
    check = txt[0]
    for i in range(0, len(txt)):
        if check == txt[i]:
            count += 1
        else:
            val += str(count)+txt[i-1]
            check = txt[i]
            count = 1
    val += str(count) + txt[-1]
    print(val)
main()
