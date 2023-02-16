"""[Recommend] Cha Cha Cha"""
import math
def main(count, total):
    """main"""
    for _ in range(count):
        num = math.ceil(float(input()))
        total += num * 8720
    print(total)
main(int(input()), 0)
