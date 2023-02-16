"""All_Primes"""
def check(num):
    """check"""
    result = True
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                result = False
    else:
        result = False
    return result

def main(num, ans):
    """main"""
    for i in range(1, num+1):
        if check(i):
            ans.append(i)
    print(len(ans))
main(int(input()), [])
