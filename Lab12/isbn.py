"""isbn"""
def main():
    """main"""
    num = input().replace("-", "")
    count = 10
    check = 0
    for i in num:
        if count == 1:
            break
        check += i*count
        count -= 1
    check = (-1*check)%11
    if check == num[-1]:
        print("Yes")
    else:
        if check == 10:
            print("No X")               
main()
