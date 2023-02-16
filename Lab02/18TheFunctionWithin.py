"""function"""
 
def function_f(num_x1):
    """F1"""
    x_of_f = 2*num_x1
    return x_of_f
 
def function_g(num_x2):
    """F2"""
    x_of_g = (3*(num_x2**4)) - (num_x2**3) + (2*(num_x2**2)) + 10
    return x_of_g
 
def function_h(num1, num2, num3):
    """F3"""
    x_of_h = (num3+num1)**2 - (num1*num2) + (num2**2)
    return x_of_h
 
def function_i(num_a, num_b, num_c, num_d):
    """F4"""
    x_of_i = ((num_a**2) + (num_b**2) - (num_c**2)) / ((num_d**2) - (2*num_a*num_d) + (2*num_a))
    return x_of_i
 
def main():
    """main"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    first1(aaa)
    first2(aaa, bbb)
    first3(aaa, bbb, ccc, ddd)
    first4(aaa, bbb, ccc, ddd)
 
def first1(aaa):
    """first1"""
    a_of_f = function_f(aaa)
    ans1 = function_f(a_of_f)
    print(ans1)
 
def first2(aaa, bbb):
    """first2"""
    ans = aaa-bbb
    x_of_f = function_f(ans)
    ans1 = function_g(x_of_f)
    print(ans1)
 
def first3(aaa, bbb, ccc, ddd):
    """first3"""
    ans1 = aaa+bbb
    ans2 = aaa+ccc
    ans3 = ddd**2
    x_of_f = function_f(ans1)
    y_of_f = function_f(ans2)
    z_of_f = function_f(ans3)
    z_of_g = function_g(z_of_f)
    total = function_h(x_of_f, y_of_f, z_of_g)
    print(total)
 
def first4(aaa, bbb, ccc, ddd):
    """first4"""
    a_of_h = function_h(function_f(aaa+bbb), function_f(aaa-ccc), function_g(function_f(ddd**2)))
    b_of_g = function_g(function_f(aaa-bbb))
    c_of_f = function_f(function_f(function_f(function_f(function_f(ccc)))))
    d_of_d = ddd**8
    total = function_i(a_of_h, b_of_g, c_of_f, d_of_d)
    print(total)
 
main()