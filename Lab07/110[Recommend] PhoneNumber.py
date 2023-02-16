"""[Recommend] PhoneNumber"""
def main():
    """main"""
    num = input()
    txt = input()
    if len(num) == 10:
        if txt == "Domestic":
            print(num[0:2], num[2:6], num[6:])
        elif txt == "International":
            print("+66"+num[1], num[2:6], num[6:])
    elif len(num) == 9:
        if txt == "Domestic":
            print(num[0], num[1:5], num[5:])
        elif txt == "International":
            print("+66", num[1:5], num[5:])
main()
