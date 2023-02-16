"""Impostor"""
import json
def main():
    """main"""
    dict_val = {}
    list_dead = []
    valcopy = []
    impostor = 0
    while True:
        val = input()
        if val == "End":
            break
        elif val[0] == "{":
            dict_val.update(json.loads(val))
        elif val != "Start":
            list_dead.append(val)
    valcopy = dict_val.copy()
    for i in list_dead:
        dict_val.pop(i)
    for i in dict_val:
        if dict_val[i] == "Impostor":
            impostor += 1
    print("%s Impostor Remains" %impostor)
    print("***Alive***")
    for i in sorted(dict_val):
        print("%s : %s" %(i, dict_val[i]))
    print("***Dead***")
    for i in sorted(list_dead):
        print("%s : %s" %(i, valcopy[i]))
main()
