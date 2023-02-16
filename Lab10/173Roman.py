"""Roman"""
def main():
    """main"""
    roman = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    txt = input()
    ans = 0
    for i in range(len(txt)):
        val = roman[txt[i]]
        if i+1 < len(txt) and roman[txt[i+1]] > val:
            ans -= val
        else:
            ans += val
    print(ans)
main()
