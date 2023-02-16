"""Run Length Decoding"""
def main():
    """main"""
    txt = input()
    val = ""
    for i in txt:
        if i.isnumeric():
            val += i
        else:
            print(i * int(val), end="")
            val = ""
main()
