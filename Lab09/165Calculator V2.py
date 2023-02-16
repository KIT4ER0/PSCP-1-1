"""Calculator V2"""
def main(num, total):
    """main"""
    if num == "1":
        total = "1"
        print(total)
    else:
        total = (len(num)+1)*int(num)
        for i in range(len(num)-1):
            move = 9*(int('1'*(i+1)))
            total -= move
        print(total)
main(input(), "")
