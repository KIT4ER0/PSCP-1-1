"""Meteorite"""
def main(met, more_met, safe):
    """main"""
    count, total = 0, 0
    if met < safe:
        total = 0
    else:
        while not met < safe:
            met = met/more_met
            total += more_met**count
            count += 1
    print(total)
main(float(input()), int(input()), float(input()))
