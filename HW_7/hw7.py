########################################################
# Intro to CS - Assignment 7
# replace the exception raising in each function with your solution
################### GOOD LUCK ##########################
########################################################
import math

import matplotlib.pyplot as plt
import sympy
from sympy import *
from functools import reduce
import operator


############ A ############
def float_range(begin=0, end=10, step=0.1):
    return [round(begin + n * step, 2) for n in range(int((end - begin) / step) + 1)]


############ B1 ############
def create_quadratic_equation(symbol, a, b, c):
    return a * symbol ** 2 + b * symbol + c


############ B2 ############
def concatenating_expressions(exprs):
    return sum(exprs)


############ B3 ############
def string_to_expressions(str_exprs):
    return [sympy.parse_expr(i.strip()) for i in str_exprs.split(',')]


############ B4 ############
def sub_in_expr(expr, symbol):
    return lambda x: expr.subs(symbol, x)


############ C ############
def plot_expr(expr, symbol, start, end, step=1):
    x_values = float_range(start, end, step)
    y_values = [expr.subs(symbol, x) for x in x_values]
    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f'A GRAPH OF THE FUNCTION: Y ={expr}')
    plt.grid()
    plt.show()


############ D1 ############
def derivative_func_recursive(expr, symbol, num):
    if num == 0:
        return expr
    else:
        h = symbols("h")
        expr = limit((((sub_in_expr(expr, symbol)(symbol + h)) - sub_in_expr(expr, symbol)(symbol)) / h), h, 0)
        return derivative_func_recursive(expr, symbol, num - 1)


############ D2 ############
def graph_of_2_derivatives(expr, symbol, start, end, step=1):
    x_1_values = float_range(start, end, step)
    y_1_values = [expr.subs(symbol, x) for x in x_1_values]
    plt.plot(x_1_values, y_1_values, label="f(x)")

    expr_1 = derivative_func_recursive(expr, symbol, 1)
    x_2_values = float_range(start, end, step)
    y_2_values = [expr_1.subs(symbol, x) for x in x_2_values]
    plt.plot(x_2_values, y_2_values, label="f'(x)")

    expr_2 = derivative_func_recursive(expr, symbol, 2)
    x_3_values = float_range(start, end, step)
    y_3_values = [expr_2.subs(symbol, x) for x in x_3_values]
    plt.plot(x_3_values, y_3_values, label="f''(x)")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f'TWO DERIVATIVES OF THE FUNCTION: Y ={expr}')
    plt.grid()
    plt.legend()
    plt.show()


############ E ############
def integral_func(expr, symbol, h=0.001):
    return lambda a, b: round(reduce(operator.add, [h * expr.subs(symbol, a + (h * i)) for i in range(int(math.floor((b-a)/h)))]), 3)


#################### Tests ##############################

x = symbols("x")
y = symbols("y")
e = symbols("e")

############ A ############
# print(float_range(0, 10, 0.5))
# print(float_range(-1, 1, 0.11))
############ B1 ############
# create_quadratic_equation(x, 1, 2, 3)
# create_quadratic_equation(x, 0, 1, 1)

############ B2 ############
# concatenating_expressions([x+2, 3*x**2, 69, 4*x, -5.5*x + 1/x])
# concatenating_expressions([x, x, x, x, x, x])

############ B3 ############
# string_to_expressions("x+3, x*x, cos(x)")
# string_to_expressions("x*x*x, sin(x)**2")

############ B4 ############
# func_1 = sub_in_expr(x**2, x)
# func_2 = sub_in_expr(cos(x), x)
# func_3 = sub_in_expr(sin(x), x)
# print(func_1(x))
# print(func_2(0))
# print(func_3(2))

############ C #############
# plot_expr(x**2, x, -5, 5, 1)
# plot_expr((x**3 + 3*x**2 - 6*x -10)/6, x, -5, 5, 0.1)
# plot_expr(cos(x), x, 0, 100, 0.1)

############ D1 ############
# print(derivative_func_recursive(x**3 + 3*x + 2, x, 2))
# derivative_func_recursive(x**2 + 3*x + 2, x, 2)
# derivative_func_recursive(x**2 + 3*x + 2, x, 3)
# derivative_func_recursive(cos(y) + y*sin(x), y, 1)
# derivative_func_recursive(cos(y) + y*sin(x), y, 2)
# derivative_func_recursive(cos(y) + y*sin(x), y, 3)
# derivative_func_recursive(10**(sinh(x)/atan(x)), x, 1)


############ D2 ############
# graph_of_2_derivatives((x**3 + 3*x**2 - 6*x - 10)/6, x, -5, 5, 0.1)
# graph_of_2_derivatives(cos(x), x, -10, 10, 0.1)

############ E #############
# print(integral_func(x**2, x)(0, 1))
# print(integral_func(x**2, x)(0, 2))

