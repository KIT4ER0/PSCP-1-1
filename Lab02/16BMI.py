"""bmi"""
 
def main():
    """main"""
    name1 = input()
    weight1 = float(input())
    height1 = float(input())
    name2 = input()
    weight2 = float(input())
    height2 = float(input())
    name3 = input()
    weight3 = float(input())
    height3 = float(input())
    name4 = input()
    weight4 = float(input())
    height4 = float(input())
    name5 = input()
    weight5 = float(input())
    height5 = float(input())
    find_bmi1(weight1, height1, name1)
    find_bmi1(weight2, height2, name2)
    find_bmi1(weight3, height3, name3)
    find_bmi1(weight4, height4, name4)
    find_bmi1(weight5, height5, name5)
 
def cal_bmi(num1, num2):
    """คำนวณbmi"""
    bmi = (num1)/((num2/100)**2)
    return bmi
 
def find_bmi1(aaa, bbb, ccc):
    """bmi1"""
    bmi1 = cal_bmi(aaa, bbb)
    print(ccc + "'s  BMI = %.2f" %bmi1)
main()