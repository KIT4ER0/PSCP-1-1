"""CaesarV1"""
def main():
    """main"""
    num = int(input())
    txt = input()
    ans = ""
    for i in txt:
        if i.isalpha():
            if i.isupper():
                ans += chr((ord(i)+num-65)%26+65)
            else:
                ans += chr((ord(i)+num-97)%26+97)
        else:
            ans += i
    print(ans)
main()
