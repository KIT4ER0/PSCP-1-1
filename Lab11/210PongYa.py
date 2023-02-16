"""pong"""
def main():
    """main"""
    val = int(input())
    if str(val)[-1] == "3":
        print("PONG")
    elif val%3 == 0:
        print("PONG")
    else:
        print(val)
main()
