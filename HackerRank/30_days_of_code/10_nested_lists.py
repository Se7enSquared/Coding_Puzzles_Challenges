# Author: Heather Gray
# Site: Hackerrank
# Problem: https://www.hackerrank.com/challenges/nested-list/problem
# Language: Python
# Problem statement:
# given a nested list of students and grades, print the name of the
# student(s) with the 2nd lowest grades

name_list = []
# Get input
for _ in range(int(input())):
    name = input()
    score = float(input())
    name_list.append([name, score])

# init lowest, second lowest and seen_numbers variables
lowest = float(100.0)
sec_lowest = float(101.0)
seen_numbers = []
output_list = []

# for each student in the name list, if the student's score is less than the
# current lowest score, set lowest to that score
for student in name_list:
    if float(student[1]) < lowest:
        if str(student[1]) not in seen_numbers:
            sec_lowest = lowest
        lowest = float(student[1])
    elif student[1] not in seen_numbers and float(student[1]) <= sec_lowest:
        sec_lowest = float(student[1])
    seen_numbers.append(student[1])

for i in range(len(name_list)):
    if name_list[i][1] == sec_lowest:
        output_list.append(name_list[i][0])

# sort output list prior to printing according to spec
output_list.sort()

for name in output_list:
    print(name)
