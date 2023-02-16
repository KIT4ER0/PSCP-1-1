"""Heron of Alexandria"""
def area(num_a, num_b, num_c):
    """area"""
    num_s = (num_a+num_b+num_c)/2
    ans = (num_s*(num_s-num_a)*(num_s-num_b)*(num_s-num_c))**0.5
    print("%.3f" %ans)
area(float(input()), float(input()), float(input()))
