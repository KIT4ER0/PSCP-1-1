"""Median"""
def median(num):
    """median"""
    num.sort()
    size = len(num)
    if size%2 == 0:
        ans = (num[(size//2-1)] + num[(size//2)])/2
    else:
        ans = num[(size//2)]
    return ans

def main(total, num):
    """main"""
    for _ in range(total):
        num.append(int(input()))
    ans = median(num)
    print("%.1f" %ans)
main(int(input()), [])
