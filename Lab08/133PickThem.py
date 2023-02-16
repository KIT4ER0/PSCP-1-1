"""PickThem"""
import json
def main(ans, even):
    """main"""
    txt = json.loads(input())
    for i in txt:
        if int(i) % 2 == 0:
            ans.append(i)
            even = True
    if even == True:
        for i in ans:
            print(i)
    else:
        print("Nope")
main([], False)
