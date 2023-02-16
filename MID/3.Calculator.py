"""Calculator"""
def main(num, total, plus):
    """Calculator"""
    if num == 1:
        print(num)
    else:
        for i in range(1, num+1):
            total += len(str(i))
            plus += 1
        print(total+plus)
main(int(input()), 0, 0)
