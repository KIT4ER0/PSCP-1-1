"""Composite"""
 
def function_f(num):
    """function_f"""
    x_of_f = num*2
    return x_of_f
 
def function_g(num):
    """function_g"""
    x_of_g = num/2 + 1
    return x_of_g
 
def main():
    """main"""
    num0 = int(input())
    num1 = function_g(num0)
    ans1 = function_f(num1)
    num2 = function_f(num0)
    ans2 = function_g(num2)
    print("%.2f" %ans1)
    print("%.2f" %ans2)
main()