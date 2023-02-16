"""colors"""
def main(val1, val2):
    """main"""
    pri = ["Red", "Yellow", "Blue"]
    if (val1 not in pri) or (val2 not in pri):
        print("Error")
    elif val1 == val2:
        print(val1)
    elif (val1 == pri[0] and val2 == pri[1]) or (val2 == pri[0]  and val1 == pri[1]):
        print("Orange")
    elif (val1 == pri[0] and val2 == pri[2]) or (val2 == pri[0]  and val1 == pri[2]):
        print("Violet")
    elif (val1 == pri[1] and val2 == pri[2]) or (val2 == pri[1]  and val1 == pri[2]):
        print("Green")
main(input(), input())
