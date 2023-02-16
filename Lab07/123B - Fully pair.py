"""B - Fully pair?"""
def main(val, check, tot):
    """main"""
    for i in val:
        if i in check:
            continue
        if val.count(i)%2 != 0:
            tot += i
        check += i
    if len(tot) == 0:
        print("fully paired")
    else:
        print(tot)
main(input(), "", "")
