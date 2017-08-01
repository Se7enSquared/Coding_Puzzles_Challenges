# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
# return all permutations of length n of a tuple of numbers using iter tools
# output must be all uppercase, one permutation per line

from itertools import permutations

n = input()
# Split the input string and integer into list
parsed_input = n.split(' ')
# sort the string and convert to upper case
iterable_string = ''.join(sorted(parsed_input[0])).upper()
# store the # of iterations
iterations = parsed_input[1]

permutation_list = list(permutations(iterable_string, int(iterations)))

for x in permutation_list:
    print(''.join(x).upper())