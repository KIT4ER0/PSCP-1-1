"""Gram_v1"""
def main():
    """main"""
    txt = input()
    check = []
    gram = ''
    val = 0
    for i in range(len(txt)-1):
        check.append(txt[i]+txt[i+1])
    for i in check:
        if check.count(i) > val:
            gram = i
            val = check.count(i)
    print(gram)
    print(val)
main()
