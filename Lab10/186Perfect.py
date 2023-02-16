"""Perfect"""
def is_prime(num):
    """-"""
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def main():
    """main"""
    num = int(input())
    per = []
    for i in range(2, num):
        if is_prime(i):
            pernum = (2 **(i-1))*((2 **i)-1)
            if pernum > num:
                break
            elif pernum <= num and pernum not in per:
                per.append(pernum)
    print(sum(per))
main()
