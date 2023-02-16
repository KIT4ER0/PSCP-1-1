"""OneTwo"""
def cal(num):
    "cal"""
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    return cal(num-1)+cal(num-2)

def main():
    """main"""
    val = int(input())
    print(cal(val))
main()
