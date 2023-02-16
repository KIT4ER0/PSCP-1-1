"""Maxtrix"""
def main():
    """main"""
    mmm = int(input())
    nnn = int(input())
    slst = []
    ans = []
    for _ in range(mmm):
        for _ in range(nnn):
            slst.append(int(input()))
        ans.append(slst)
        slst = []
    for i in ans:
        print(*i)
main()
