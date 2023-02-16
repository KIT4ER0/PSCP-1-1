"""HorizontalHistogram"""
def cal(num, ans):
    """cal"""
    for i in range(num):
        if i%5 == 0 and i != 0:
            ans += "|"
        ans += "-"
    return ans

def main():
    """main"""
    txt = input()
    small, big = "", ""
    for i in txt:
        if i.islower():
            small += i
        else:
            big += i
    for i in sorted(set(small))+sorted(set(big)):
        print(i, ":", cal(txt.count(i), ""))
main()
