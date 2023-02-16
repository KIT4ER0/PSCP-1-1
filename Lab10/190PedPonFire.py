"""PedPonFire"""
import math
def main():
    """main"""
    val = []
    for _ in range(int(input())):
        val.append(int(input()))
    kkk = int(input())
    val.sort()
    set_val = sorted(set(val))
    check = val.count(kkk/2)
    if check <= 1:
        ans = 0
    else: ans = math.factorial(check) // (math.factorial(check - 2)* math.factorial(2))
    for i in set_val:
        if i >= kkk/2:
            break
        ans += val.count(kkk-i)*val.count(i)
    print(ans)
main()
