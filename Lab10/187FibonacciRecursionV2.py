"""FIbonacciRecursionV2"""
def fibo(num, val):
    """-"""
    if num in val:
        return val[num]
    if num > 500:
        fibo(num-500, val)
    res = fibo(num-2, val)+fibo(num-1, val)
    val[num] = res
    return res

def main():
    """main"""
    num = int(input())
    val = {0:0, 1:1}
    result = fibo(num, val)
    print(result)
main()
