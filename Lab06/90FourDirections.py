"""FourDiretions"""
def main():
    """main"""
    txt = input()
    co1 = ""
    co2 = ""
    co3 = ""
    co4 = ""
    co5 = ""
    for i in txt:
        if i == "U":
            co1 += "  *   "
            co2 += " ***  "
            co3 += "* * * "
            co4 += "  *   "
            co5 += "  *   "
        elif i == "D":
            co1 += "  *   "
            co2 += "  *   "
            co3 += "* * * "
            co4 += " ***  "
            co5 += "  *   "
        elif i == "L":
            co1 += "  *   "
            co2 += " *    "
            co3 += "***** "
            co4 += " *    "
            co5 += "  *   "
        elif i == "R":
            co1 += "  *   "
            co2 += "   *  "
            co3 += "***** "
            co4 += "   *  "
            co5 += "  *   "
    print(co1)
    print(co2)
    print(co3)
    print(co4)
    print(co5)
main()
