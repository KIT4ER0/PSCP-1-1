"""Flatten"""
import json
def main():
    """main"""
    list_num = json.loads(input())
    list_ans = []
    while list_num:
        val = list_num.pop()
        if isinstance(val, int):
            list_ans.append(val)
        else:
            list_num.extend(val)
    list_ans.sort(reverse=True)
    print(list_ans)
main()
