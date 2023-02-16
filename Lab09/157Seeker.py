"""Seeker"""
def main():
    """main"""
    txt = input()
    val = ""
    ans = 0
    for i in txt:
        if i.isdigit():
            val += i
        else:
            if val == "":
                ans += 0
            else:
                ans += int(val)
                val = ""
    if val.isdigit():
        print(ans+int(val))
    else:
        print(ans)
main()
