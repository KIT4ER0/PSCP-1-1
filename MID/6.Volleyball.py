"""Volleyball"""
def main(txt, game_set, counter):
    """main"""
    sco_a = sco_b = 0
    set_a = set_b = 0

    for team in txt:
        if team == "A":
            sco_a += 1
        else:
            sco_b += 1
        if game_set == 5 and sco_a-sco_b >= 2 and (sco_a >= 15 or sco_b >= 15):
            set_a += 1
            print("Set %d: A (%d) | B (%d)" %(game_set, sco_a, sco_b))
        elif game_set == 5 and sco_b-sco_a >= 2 and (sco_a >= 15 or sco_b >= 15):
            set_b += 1
            print("Set %d: A (%d) | B (%d)" %(game_set, sco_a, sco_b))
        elif sco_a-sco_b >= 2 and (sco_a >= 25 or sco_b >= 25):
            set_a += 1
            print("Set %d: A (%d) | B (%d)" %(game_set, sco_a, sco_b))
            game_set += 1
            sco_a = sco_b = 0
        elif sco_b-sco_a >= 2 and (sco_a >= 25 or sco_b >= 25):
            set_b += 1
            print("Set %d: A (%d) | B (%d)" %(game_set, sco_a, sco_b))
            game_set += 1
            sco_a = sco_b = 0
        elif counter+1 == len(txt):
            print("Set %d: A (%d) | B (%d)" %(game_set, sco_a, sco_b))
            game_set += 1
        counter += 1

    if set_a > set_b and set_a >= 3:
        print("A won %d:%d set" %(set_a, set_b))
    elif set_b > set_a and set_b >= 3:
        print("B won %d:%d set" %(set_b, set_a))
    else:
        if sco_a == 0 and sco_b == 0:
            print("Set %d: A (%d) | B (%d)" %(game_set, sco_a, sco_b))
        print("The game has not finished yet.")
main(input(), 1, 0)
