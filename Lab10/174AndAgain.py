"""AndAgain"""
def main():
    """main"""
    val = input().replace(".", "").split()
    ans = []
    for i in val:
        total = i.count("a") + i.count("e") + i.count("i") + i.count("o") + i.count("u")
        if total >= 2:
            ans.append(i)
    ans.sort()
    if len(ans) == 0:
        print("Nope")
    else:
        print(*ans, sep="\n")
main()
