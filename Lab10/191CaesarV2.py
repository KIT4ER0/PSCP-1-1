"""CaesarV2"""
def cal(result, words):
    """-"""
    for i in words:
        if i in result:
            return True
    return False

def main():
    """main"""
    txt = input()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    words = ['The', 'the', 'What', 'what', 'Where', 'where', 'When', 'when']
    result = ""
    while True:
        for i in txt:
            if i.isupper():
                result += upper[(upper.index(i)+1)%26]
            elif i.islower():
                result += lower[(lower.index(i)+1)%26]
            else: result += i
        txt = result
        if cal(result, words):
            break
        result = ""
    print(txt)
main()
