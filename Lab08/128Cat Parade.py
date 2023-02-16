"""Cat Parade"""
def main(kept, spec):
    """main"""
    while True:
        txt = input().split(", ")
        if txt == ["IT'S A DOG"]:
            kept.pop()
            continue
        if txt == ["END"]:
            break
        kept += txt
    for i in kept:
        if i not in spec:
            spec.append(i)
    spec.sort()
    for i in range(len(spec)):
        print("%s %d %d" %(spec[i], (kept.index(spec[i])+1), kept.count(spec[i])))
main([], [])
