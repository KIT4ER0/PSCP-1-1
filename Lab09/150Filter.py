"""Filter"""
import json
def main():
    """-"""
    dict_val = {}
    dict_val.update(json.loads(input()))
    score_filter = float(input())
    list_val = []
    for i in dict_val:
        if dict_val[i] >= score_filter:
            list_val.append(i)
    if list_val == []:
        print("Nope")
    else:
        for i in sorted(list_val):
            print("%s\t%.2f" %(i, dict_val[i]))
main()
