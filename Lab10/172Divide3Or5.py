"""Divide3Or5"""
def main(num, total):
    """main"""
    for i in range(1, num+1):
        if i%3 == 0 or i%5 == 0:
            total += i
    print(total)
main(int(input()), 0)
