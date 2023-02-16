"""BrickBridge"""
def main():
    """main"""
    numa = int(input())
    numb = int(input())
    numg = int(input())
    if numa < numg%5:
        print(-1)
    elif numa+(numb*5) < numg:
        print(-1)
    else:
        if numb*5 >= numg:
            small = numg%5
        else:
            small = numg-(numb*5)
        print(small)
main()