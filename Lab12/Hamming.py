"""Hamming"""
def main():
    """main"""
    txt1 = input()
    txt2 = input()
    count = 0
    for i in range(len(txt1)):
        if txt1[i] != txt2[i]:
            count += 1
    print(count)
main()
