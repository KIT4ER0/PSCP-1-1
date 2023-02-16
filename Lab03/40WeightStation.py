"""WeightStation"""
def main():
    """main"""
    avg = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    weight4 = (avg*4)-(weight1+weight2+weight3)
    sumweight = weight1+weight2+weight3+weight4
    little = avg-(avg/2)
    many = avg+(avg/2)
    if sumweight > 15000:
        print("Overweight")
    elif many > weight1 > little and many > weight2 > little and many > weight3 > little\
        and many > weight4 > little:
        print("Pass %.2f" %weight4)
    else:
        print("Unbalance")
main()