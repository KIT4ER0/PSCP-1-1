"""isPrime_large"""
def cal(num):
    """-"""
    if num == 1:
        return "NO"
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return "NO"
    return "YES"

def main():
    """main"""
    num = int(input())
    print(cal(num))
main()
