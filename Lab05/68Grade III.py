"""Grade III"""
def main():
    """main"""
    all_subject = int(input())
    sco_total = 0
    for _ in range(all_subject):
        subject = float(input())
        sco_total += grade(subject)
    sco_total = int((sco_total/all_subject)*100)/100
    print("%.2f" %sco_total)

def grade(score):
    """score"""
    mark = 0
    if 95 <= score <= 100:
        mark = 4
    elif 90 <= score < 95:
        mark = 3.5
    elif 85 <= score < 90:
        mark = 3
    elif 80 <= score < 85:
        mark = 2.5
    elif 75 <= score < 80:
        mark = 2
    elif 70 <= score < 75:
        mark = 1.5
    elif 65 <= score < 70:
        mark = 1
    elif 60 <= score < 65:
        mark = 0.5
    elif 0 <= score < 60:
        mark = 0
    return mark
main()
