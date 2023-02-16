"""PickThemAgain"""
def main(x_val, val, t_or_f):
    """main"""
    val.reverse()
    for i in val:
        if int(i)% 3 == 0 or int(i)% 5 == 0:
            x_val.append(i)
            t_or_f = True
    if t_or_f == True:
        for i in x_val:
            print(i)
    else:
        print("Nope")
main([], input().split(" "), False)
