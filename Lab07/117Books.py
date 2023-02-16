"""Books"""
import math
def main(num1, num2, num3, num4):
    """main"""
    count = 0
    day = 0
    couter = 0
    while True:
        num5 = math.ceil((num3/num4)*num2)
        if count == num1:
            break
        if num5 >= num2:
            break
        couter += num5
        if couter >= num2:
            couter = 0
            count += 1
        num3 += 1
        num4 += 1
        day += 1
    day += num1-count
    print(day)
main(int(input()), int(input()), int(input()), int(input()))
