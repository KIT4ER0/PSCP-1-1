"""day"""
def main():
    """main"""
    year = float(input())
    if year%4 != 0:
        print("No")
    elif year%4 == 0 and year%100 != 0:
        print("Yes")
    elif year%4 == 0 and year%100 == 0 and year%400 == 0:
        print("Yes")
    else:
        print("No")
main()