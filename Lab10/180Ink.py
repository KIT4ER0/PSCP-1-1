"""INK"""
import math
def main():
    """main"""
    area_ink, num_people = [int(i) for i in input().split()]
    area_ans = []
    for _ in range(num_people):
        xxx, yyy = [int(i) for i in input().split()]
        result = 3.1416*((xxx**2 + yyy**2)**0.5)**2
        area_ans.append(result)
    for i in area_ans:
        print(math.ceil(i/area_ink))
main()
