"""BTSMRT"""
def main():
    """main"""
    txt = input()
    age = float(input())
    height = float(input())
    if txt == "Children Day":
        if age < 14 and height <= 140:
            print("FREE")
        else:
            print("PAY")
    elif txt == "Senior Day":
        if age >= 60:
            print("FREE")
        elif age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
    elif txt == "Normal Day":
        if age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
main()
