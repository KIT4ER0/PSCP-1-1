"""Turnstile"""
def main():
    """main"""
    txt = ""
    people = 0
    coin = 0
    while True:
        if txt != "END":
            txt = input()
        else:
            break
        if txt == "C":
            coin = 1
        if txt == "P":
            if coin == 1:
                people += 1
            coin = 0
    print(people)
main()
