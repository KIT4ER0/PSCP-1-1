"""ProgressiveTax"""
def main():
    """main"""
    num = int(input())
    total = 0
    if num > 4000000:
        total += (num-4000000)*0.35
        num -= num-4000000
    if num > 2000000:
        total += (num-2000000)*0.30
        num -= num-2000000
    if num > 1000000:
        total += (num-1000000)*0.25
        num -= num-1000000
    if num > 750000:
        total += (num-750000)*0.20
        num -= num-750000
    if num > 500000:
        total += (num-500000)*0.15
        num -= num-500000
    if num > 300000:
        total += (num-300000)*0.10
        num -= num-300000
    if num > 150000:
        total += (num-150000)*0.05
        num -= num-150000
    if num > 0:
        pass
    print("%d" %total)
main()
