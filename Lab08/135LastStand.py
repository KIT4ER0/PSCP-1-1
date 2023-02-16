"""LastStand"""
def main(val):
    """main"""
    val = val.replace("[", "")
    val = val.replace("]", "")
    val = val.split(",")
    for i in val:
        print(i[-1])
main(input())
