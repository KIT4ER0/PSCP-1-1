"""Virus I"""
def main():
    """main"""
    txt = input()
    count = 0
    for i in txt:
        if i == "o":
            count += 1
    print(count)
main()
