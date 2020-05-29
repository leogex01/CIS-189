"""Program: cast_to_integer.py
Author: Chris Geralds
Last date modified:05/29/2020

The purpose of this program is to accept any input, 
convert to a integer type and output the integer. 
"""
random_input = input("Enter anything to see if it converts to an integer: ")
print(int(random_input))

""" 
The only string you can pass to int() that will work is a string representation of an integer. 
A non-integer string will give a "ValueError: invalid literal for int() with base 10:"FOO"

"""
# Test  Expected Results  Actual Output
# 7      7                 7
# 6.7    6                 Error mentioned above
# ABC    ValueError        Error mentioned above