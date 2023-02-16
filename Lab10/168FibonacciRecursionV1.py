"""FibonacciRecursionV1"""
def fibonacci(num):
    """Fibonacci"""
    if num <= 0:
        return abs(num)
    return fibonacci(num-1) + fibonacci(num-2)

def main():
    """main"""
    val = int(input())
    print(fibonacci(val))
main()
