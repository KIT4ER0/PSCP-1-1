"""ClockHands"""
def main():
    """main"""
    hours = int(input())
    mins = int(input())
    hours = ((hours*5) + (mins/12)) % 60
    ans = "True" if mins <= hours < mins+1 else "False"
    print(ans)
main()
