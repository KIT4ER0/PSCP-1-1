"""MAC"""
def main(val):
    """main"""
    if not (len(val) == 17 or len(val) == 14):
        return print("ERROR")
    character = "ABCDEFabcdef1234567890.:-"
    for i in val:
        if i not in character:
            return print("ERROR")
    if not (val.count("-") == 5 or val.count(":") == 5 or val.count(".") == 2):
        return print("ERROR")
    if val[2] == "-" and val[5] == "-" and val[8] == "-" and val[11] == "-" and val[14] == "-":
        print("VALID 1")
    elif val[2] == ":" and val[5] == ":" and  val[8] == ":" and val[11] == ":" and val[14] == ":":
        print("VALID 2")
    elif val[4] == "." and val[9] == "." and val[:4].isalnum()\
         and val[5:9].isalnum() and val[10:].isalnum():
        print("VALID 3")
    else:
        print("ERROR")
main(input())
