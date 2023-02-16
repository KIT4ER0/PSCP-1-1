"""SMS"""
def main():
    """main"""
    list_txt = [
        ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"],
        ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"],
        ["T", "U", "V"], ["W", "X", "Y", "Z"]
    ]
    ans = []
    for _ in range(int(input())):
        num = int(input())
        val = int(input())
        if num == 1:
            for _ in range(val):
                if len(ans) > 0:
                    ans.pop()
        if num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 8 and val != 0:
            if val%3 == 0:
                ans.append(list_txt[num-2][2])
            else: ans.append(list_txt[num-2][(val%3)-1])
        if num == 7 or num == 9:
            if val%4 == 0:
                ans.append(list_txt[num-2][3])
            else: ans.append(list_txt[num-2][(val%4)-1])
    if len(ans) > 0:
        return print(*ans, sep="")
    print("null")
main()
