"""AscendingSort"""
def main():
    """main"""
    num = []
    for _ in range(5):
        num.append(int(input()))
    num.sort()
    for ans in num:
        print(ans)
main()
