"""BookWorm"""
def main(num_set):
    """main"""
    for _ in range(num_set):
        mins = float(input())
        val = sorted([float(input()) for _ in range(int(input()))])
        i = 0
        for i in range(len(val)):
            if sum(val[:i+1]) > mins:
                break
            i += 1
        print(i)
main(int(input()))