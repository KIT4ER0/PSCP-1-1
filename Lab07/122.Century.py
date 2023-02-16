"""Century"""
import math
def cal(year):
    """cal"""
    if year < 1:
        return "ERROR"
    elif 1 <= year <= 100:
        return 1
    else:
        return int(math.ceil(year/100))

def main(num):
    """main"""
    for _ in range(num):
        txt = input()
        if txt[:4] == "B.E.":
            year = int(txt[5:])-543
            print(cal(year))
        elif txt[:4] == "A.D.":
            year = int(txt[5:])
            print(cal(year))
main(int(input()))
