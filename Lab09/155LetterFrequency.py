"""LetterFrequency"""
def main():
    """main"""
    txt = input().lower().replace(" ", "")
    kept = {}
    for i in set(txt):
        kept[i] = txt.count(i)
    print(max(kept, key=txt.count))
main()
