"""BigFrame"""
def main(txt1, txt2, txt3, txt4, txt5):
    """main"""
    most = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    print("**" + "*"*most + "**")
    print("* " + txt1 + " "*(most-len(txt1)) + " *")
    print("* " + txt2 + " "*(most-len(txt2)) + " *")
    print("* " + txt3 + " "*(most-len(txt3)) + " *")
    print("* " + txt4 + " "*(most-len(txt4)) + " *")
    print("* " + txt5 + " "*(most-len(txt5)) + " *")
    print("**" + "*"*most + "**")
main(input().rstrip(), input().rstrip(), input().rstrip(), input().rstrip(), input().rstrip())
