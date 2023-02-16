"""VerticalHistogram"""
def main():
    """main"""
    txt = input()
    kept = ""
    remain = ""
    for i in txt:
        if i.islower():
            kept += i
        else: remain += i
    kept = sorted(set(kept))+sorted(set(remain))
    count = [txt.count(i) for i in kept]
    for i in range(max(count), 0, -1):
        print("%03d" %i, end="")
        for j in count:
            if j >= i:
                print(" *", end="")
            else: print("  ", end="")
        print()
    print("   ", end="")
    for i in kept:
        print(" %s" %i, end="")
main()
