"""Harshad"""
def main():
    """main"""
    for _ in range(10):
        num = int(input())
        if num == 0:
            print("No")
        elif len(str(num)) == 1:
            if num%num == 0:
                print("Yes")
            else:
                print("No")
        else:
            if num%cal(num) == 0:
                print("Yes")
            else:
                print("No")

def cal(num):
    """cal"""
    count = 0
    num = str(num)
    if int(num) < 0:
        for i in num[1:]:
            count += int(i)
        count *= -1
    else:
        for i in num:
            count += int(i)
    return count

main()
