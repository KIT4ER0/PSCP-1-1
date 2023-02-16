"""print"""
def main():
    """print"""
    num = 492137954293754252786
    mil = num
    sec = mil//1000
    mil = mil%1000
    mins = sec//60
    sec = sec%60
    hour = mins//60
    mins = mins%60
    day = hour//24
    hour = hour%24
    print(day, hour, mins, sec, mil)
main()