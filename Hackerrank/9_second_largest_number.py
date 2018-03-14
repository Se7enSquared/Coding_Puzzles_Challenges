# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
#   You are given n numbers. Store them in a list and find the second largest
#  number.

# Size of array
n = int(input())
# n numbers separated by space
arr = map(int, input().split())

# initialized very low to catch negative numbers. -101 based on problem
# constraint of numbers between -100 and 100
greatest = -101
second_greatest = -101
seen_numbers = []
for number in arr:
    if int(number) > greatest:
        if str(number) not in seen_numbers:
            second_greatest = greatest
        greatest = number
    elif number not in seen_numbers and int(number) >= second_greatest:
        second_greatest = number
    seen_numbers.append(number)
print(second_greatest)