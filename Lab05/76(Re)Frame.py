"""Frame"""
def main():
    """main"""
    text = input()
    aaa(text)
    bbb(text)
    aaa(text)

def aaa(txt):
    """aaa"""
    print("*" + (len(txt)*"*") + "*")

def bbb(txt):
    """bbb"""
    print("*" + txt + "*")
main()
