"""Pringles"""
def main(top, center, bottom, num):
    """main"""
    eat_c = 0
    leave_c = 0
    eat = center[:num:]
    leave = center[num:]
    for i in eat:
        if i == ")":
            eat_c += 1
    for j in leave:
        if j == ")":
            leave_c += 1
    print(eat_c)
    if leave_c == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(top)
    print("%s%s" %((" "*num), leave))
    print(bottom)
main(input(), input(), input(), int(input()))
