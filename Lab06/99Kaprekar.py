"""Kaprepar"""
def main():
    """main"""
    num = input()
    count = 0
    out = 0
    total = total_num(num)
    while out != 6174:
        low = int(total[0]+total[1]+total[2]+total[3])
        high = int(total[3]+total[2]+total[1]+total[0])
        out = high - low
        total = total_num(str(out).zfill(4))
        count += 1
    print(count)

def total_num(num):
    """total"""
    num_a, num_b, num_c, num_d = int(num[0]), int(num[1]), int(num[2]), int(num[3])
    if num_a > num_b:
        num_a, num_b = num_b, num_a
    if num_c > num_d:
        num_c, num_d = num_d, num_c
    if num_a > num_c:
        num_a, num_c = num_c, num_a
    if num_b > num_d:
        num_b, num_d = num_d, num_b
    if num_b > num_c:
        num_b, num_c = num_c, num_b
    return str(num_a), str(num_b), str(num_c), str(num_d)
main()
