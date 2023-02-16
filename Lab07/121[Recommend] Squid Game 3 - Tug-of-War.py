"""[Recommend] Squid Game 3 - Tug-of-War"""
def main():
    """main"""
    team_a = 0
    team_b = 0
    for _ in range(10):
        team_a += int(input())
    for _ in range(10):
        team_b += int(input())
    if team_a < team_b:
        print("A")
    elif team_b < team_a:
        print("B")
    else:
        print("AB")
main()
