"""SecondConverter"""
def main():
    """main"""
    kkk = int(input())
    sss = int(input())
    mmm = int(input())
    hhh = int(input())
    second = kkk%sss
    mins = kkk//sss
    hour = mins//mmm
    mins = mins%mmm
    hour = hour%hhh
    print("%d:%d:%d" % (hour, mins, second))
main()
