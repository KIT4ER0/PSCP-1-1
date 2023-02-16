"""CircularPrime"""
def is_prime(num):
    """-"""
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def circular(num):
    """-"""
    if not is_prime(num):
        return 0
    num_str = str(num)
    digits = len(num_str)-1
    for _ in range(digits):
        num_str = num_str[-1]+num_str[:-1]
        if not is_prime(int(num_str)):
            return 0
    return num

def main():
    """main"""
    num = int(input())
    print(sum([circular(i) for i in range(1, num+1)]))
main()
