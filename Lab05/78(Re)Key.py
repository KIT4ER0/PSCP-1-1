"""Key"""
def main():
    """main"""
    num = input()
    total = 0
    for i in num:
        total += int(i)
    threelast = int(num[-3:])*10
    tot = total + threelast
    if tot > 1000:
        print(str(tot)[-4:])
    else:
        tot += 1000
        print(str(tot))
main()
