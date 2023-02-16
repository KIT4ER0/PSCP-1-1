"""Difference"""
def main(all_a, all_b, set_a, set_b):
    """main"""
    for _ in range(all_a):
        set_a.add(int(input()))
    for _ in range(all_b):
        set_b.add(int(input()))
    for ans in sorted(set_a-set_b):
        print(ans, end=" ")
main(int(input()), int(input()), set(), set())
