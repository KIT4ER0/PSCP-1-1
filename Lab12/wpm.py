"""wpm"""
def main():
    """main"""
    val = input()
    num = int(input())
    ans = ""
    if val == "Kids":
        if num < 11:
            ans = "Very Slow"
        elif 11 <= num <= 20:
            ans = "Slow"
        elif 21 <= num <= 30:
            ans = "Average"
        elif 31 <= num <= 40:
            ans = "Fast"
        else: ans = "Very Fast"
    else:
        if num < 26:
            ans = "Very Slow"
        elif 26 <= num <= 35:
            ans = "Slow/Beginner"
        elif 36 <= num <= 45:
            ans = "Intermediate/Average"
        elif 46 <= num <= 65:
            ans = "Fast/Advanced"
        elif 66 <= num <= 80:
            ans = "Very Fast"
        else: ans = "Insane"
    print(ans)
main()
