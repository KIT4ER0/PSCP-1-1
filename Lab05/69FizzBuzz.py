"""FizzBuzz"""
def main():
    """main"""
    num = int(input())
    i = 1
    while True:
        if i < num+1:
            if i%3 == 0 and i%5 == 0:
                print("FizzBuzz")
            elif i%3 == 0:
                print("Fizz")
            elif i%5 == 0:
                print("Buzz")
            else:
                print(i)
        else:
            break
        i += 1
main()
