"""Diamond I"""
def main(deep, large, val, ans):
    """main"""
    for _ in range(deep):
        diamond = input().split()
        val.append(diamond)
    for i in range(large):
        result = 0
        for j in val:
            result += int(j[i])
        ans.append(result)
    print(max(ans))
main(int(input()), int(input()), [], [])
