"""SurprisingVote"""
def main():
    """main"""
    totnum = float(input())
    mxnum = float(input())
    num2 = 0
    if mxnum * 2 < totnum:
        num2 = totnum - mxnum * 2
    if mxnum - num2 > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
