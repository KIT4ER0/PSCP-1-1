"""AlmostMean"""
def main(total, list_data, list_score):
    """main"""
    for i in range(total):
        txt = input().split("\t")
        list_data.append(txt[0])
        list_score.append(float(txt[1]))
    mean = (sum(list_score))/total
    result = list_score[:]
    list_score.sort(reverse=True)
    for i in list_score:
        if float(i) < mean:
            ans = (list_score.index(i))
            result = (result.index(i))
            print(str(list_data[result])+"\t"+str(list_score[ans]))
            break
main(int(input()), [], [])
