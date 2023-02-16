"""tax"""
def main(agecar, sizecar, cc1, cc2, cc3):
    """main"""
    if sizecar <= 600:
        cc1 = sizecar*0.5
    elif 601 <= sizecar <= 1800:
        cc1 = 300
        cc2 = (sizecar-600)*1.5
    elif sizecar >= 1801:
        cc1 = 300
        cc2 = 1800
        cc3 = (sizecar-1800)*4
    ans = cc1+cc2+cc3
    if agecar == 6:
        ans = ans-(ans*10/100)
    elif agecar == 7:
        ans = ans-(ans*20/100)
    elif agecar == 8:
        ans = ans-(ans*30/100)
    elif agecar == 9:
        ans = ans-(ans*40/100)
    elif agecar >= 10:
        ans = ans-(ans*50/100)
    print("%.2f" %ans)
main(int(input()), int(input()), 0, 0, 0)
    