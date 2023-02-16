"""Duplicate I"""
def main(all_a, all_b, set_a, set_b):
    """main"""
    for _ in range(all_a):
        set_a.add(int(input()))
    for _ in range(all_b):
        set_b.add(int(input()))
    if len(set_a&set_b) == 0:
        print("Nope")
    else:
        print(*sorted(set_a&set_b, reverse=True), sep="\n")
main(int(input()), int(input()), set(), set())
