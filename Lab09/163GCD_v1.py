"""GCD_v1"""
def main(num_a, num_b):
    """main"""
    for i in range(100000, 0, -1):
        if num_a%i == 0 and num_b%i == 0:
            print(i)
            break
main(int(input()), int(input()))
