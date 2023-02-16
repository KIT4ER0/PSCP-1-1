"""Point Sorting"""
def sort_y(point):
    """y"""
    return int(point[1])

def sort_xy(point):
    """xy"""
    sum_point = int(point[0])+int(point[1])
    return sum_point

def main(total):
    """main"""
    for _ in range(total):
        val = []
        for _ in range(int(input())):
            val.append(input().split())
        val.sort(key=sort_y, reverse=True)
        val.sort(key=sort_xy)
        for i in val:
            print(*i)
main(int(input()))
