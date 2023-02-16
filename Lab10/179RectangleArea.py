"""RectangleArea"""
def main():
    """main"""
    ax2, ay2, width1, height1 = [int(i) for i in input().split()]
    bx2, by2, width2, height2 = [int(i) for i in input().split()]
    ax1, ay1 = ax2+width1, ay2+height1
    bx1, by1 = bx2+width2, by2+height2
    width = max(0, min(ax1, bx1)- max(ax2, bx2))
    height = max(0, min(ay1, by1)- max(ay2, by2))
    print(width*height if width*height > 0 else "no overlapping")
main()
