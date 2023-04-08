# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:10:09 2023
function tutorial 
@author: jacob
"""
def add(x,y):
    return x + y
def multiply(x,y):
    return x * y

def do_math(action, x, y):
    return action(x,y)

print(add(3,4))
print(multiply(3,4))
print(do_math(add, 3, 4))
print(do_math(multiply, 3,4))

my_list = [1,2,3,4]

double_list = [2*val for val in my_list]
print(my_list)
print(double_list)