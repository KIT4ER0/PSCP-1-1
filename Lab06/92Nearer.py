"""Nearer"""
def main():
    """main"""
    numa = int(input())
    numb = int(input())
    numi = int(input())
    if abs(numi-numa) < abs(numi-numb):
        print("Alice", abs(numi-numa))
    elif abs(numi-numa) > abs(numi-numb):
        print("Bob", abs(numi-numb))
    elif abs(numi-numa) == abs(numi-numb):
        print("Sundaes", abs(numi-numa))
main()
