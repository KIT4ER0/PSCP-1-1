"""BreachTheDoor"""
def main():
    """main"""
    txt = input().split()
    ans = []
    for i in txt:
        for j in i:
            if not j.isidentifier():
                i = i.replace(j, "")
        ans.append(i)
    print(*(list(filter(lambda i: len(i) > 6, ans))))
main()
