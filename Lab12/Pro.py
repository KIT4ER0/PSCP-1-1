"""Pro"""
def main():
    """main"""
    prox = int(input())
    proy = int(input())
    peoa = int(input())
    peoz = int(input())
    money = (peoz//prox)*proy*peoa
    money += (peoz%prox)*peoa
    print(money)
main()
