# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
# Read two integers and print two lines.
# The first line should contain integer division,  a//b .
# The second line should contain float division,  a/b .
# You don't need to perform any rounding or formatting operations.

def int_div(a, b):
    return a // b

def float_div(a, b):
    return a/b

print(int_div(a, b))
print(float_div(a, b))