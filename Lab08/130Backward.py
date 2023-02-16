"""Backward"""
def main():
    """main"""
    txt = []
    i = input()
    while i != "NULL":
        txt.append(i)
        i = input()
    for ans in reversed(txt):
        print(ans)
main()
