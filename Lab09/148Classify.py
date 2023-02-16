"""Classify"""
def main(id_std, o_year):
    """main"""
    while True:
        val = input()
        if val == "END":
            break
        id_std.append(val[:4])
    for i in sorted(set(id_std)):
        group = int(i[2:4])
        year = i[:2]
        if year != o_year:
            print(year, group, id_std.count(i))
        else:
            print("--", group, id_std.count(i))
        o_year = year
main([], 0)
