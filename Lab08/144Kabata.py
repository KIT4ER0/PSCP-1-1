"""Kabata"""
def main(total):
    """main"""
    for _ in range(total):
        txt = input()
        txt = txt.replace('baka', '-').replace("bakka", "").replace("ta", "").replace("ba", "").\
            replace("ka", "")
        if txt == "":
            print("yes")
        else:
            print("no")
main(int(input()))
