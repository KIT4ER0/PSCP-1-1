"""Day2011"""
def main():
    """main"""
    day = int(input())
    month = int(input())
    num = 0
    last = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    for i in range(month):
        num += last[i]
    val = (num+day)%7
    if val == 1:
        print("Saturday")
    elif val == 2:
        print("Sunday")
    elif val == 3:
        print("Monday")
    elif val == 4:
        print("Tuesday")
    elif val == 5:
        print("Wednesday")
    elif val == 6:
        print("Thursday")
    else:
        print("Friday")
main()
