"""LineSorting"""
def main(total, txt):
    """main"""
    for _ in range(total):
        txt.append(input())
    txt = sorted(txt, key=lambda x: (len(x), x))
    for i in txt:
        print(i)
main(int(input()), [])
