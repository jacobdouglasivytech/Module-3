# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:17:52 2023

@author: jacob
"""

class do_math:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        
    def add(self):
        return self.val1 + self.val2
    
    def multiply(self):
        return self.val1 * self.val2
    
    def double_input(self):
        self.val1 *= 2
        self.val2 *= 2
    
math_instance = do_math(3,4)
print(math_instance.add())
print(math_instance.multiply())
print(math_instance.double_input())
print(math_instance.add())
