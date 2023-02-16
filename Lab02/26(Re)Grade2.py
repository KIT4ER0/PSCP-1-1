"""grade"""
def main():
    """main"""
    num = float(input())
    if 0 <= num < 60:
        print("F")
    elif 60 <= num < 65:
        print("F+")
    elif 65 <= num < 70:
        print("D")
    elif 70 <= num < 75:
        print("D+")
    elif 75 <= num < 80:
        print("C")
    elif 80 <= num < 85:
        print("C+")
    elif 85 <= num < 90:
        print("B")
    elif 90 <= num < 95:
        print("B+")
    elif 95 <= num <= 100:
        print("A")
    elif num > 100 or num < 0:
        print("ERR")
main()