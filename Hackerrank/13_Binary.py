#   date : 2/2/2019
#   author : H. Gray
#   email : heathergray153@gmail.com
#
#   title : Binary Numbers
#   brief : Given a base- integer, , convert it to binary (base-). 
#           Then find and print the base- integer denoting the maximum number
#           of consecutive 's in 's binary representation.
#
#   source : https://www.hackerrank.com/challenges/30-binary-numbers/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(439)
    # set up

    binary_digit = n % 2
    divisor = n // 2
    binary_list = []
    binary_list.insert(0, binary_digit)
    # loop to continue converting binary numbers
    while divisor // 2 != 0:
        binary_digit = divisor % 2
        divisor = divisor // 2
        binary_list.insert(0, binary_digit)
    binary_digit = divisor % 2
    binary_list.insert(0, binary_digit)
    print(binary_list)

    list_of_1 = []
    sum_of_1 = 0
    
    for number in binary_list:
        if number == 1:
            sum_of_1 += 1
        else:
            list_of_1.append(int(sum_of_1))
            sum_of_1 = 0
            continue
        list_of_1.append(sum_of_1)
    
    print(max(list_of_1))
