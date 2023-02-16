"""SceneSwitch I"""
def main(turn, warm, count, last):
    """main"""
    while True:
        time = input()
        if time == "End":
            break
        time = float(time)
        if time == 0:
            turn = 1
            continue
        elif turn == 1:
            turn, last = 0, time
            continue
        elif turn == 0 and time-last > 6:
            warm, turn = 0, 1
        elif turn == 0 and time-last <= 6 and warm == 0:
            warm, turn = 1, 1
            count += 1
        elif turn == 0 and time-last <= 6 and warm == 1:
            warm, turn = 0, 1
    print(count)
main(0, 0, 0, 0)
