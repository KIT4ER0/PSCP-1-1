"""WordSequence I"""
def main(txt):
    """main"""
    for ans in range(len(txt)):
        print(txt[:ans+1])
main(input())
