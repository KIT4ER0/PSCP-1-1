"""Heads and Legs"""
def main():
    """main"""
    animal = int(input())
    all_legs = int(input())
    rabbit, ghost = divmod(all_legs-2*animal, 2)
    bird = animal-rabbit
    if rabbit >= 0 and bird >= 0 and ghost == 0:
        print(rabbit, bird)
    else: print("Impossible")
main()
