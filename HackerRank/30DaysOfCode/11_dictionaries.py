#   date : 8/27/2017
#   author : H. Gray
#   email : heathergray153@gmail.com
#
#   title : Dictionaries
#   brief : given an integer, N and a list of entries and lookup values,
#           compile a dictionary then return the values for the given entry lookups. If an entry
#           is not in the dict, return 'not found'
#
#   source : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

phone_book = {}
input_list = []
lookup_list = []
N = int(input())

# create input and lookup lists from stdin
for x in range(N):
    input_list.append(input().split())
for z in range(N):
    lookup_list.append(input())

# create dictionary
for data in input_list:
    phone_book[data[0]] = data[1]

# return values based on lookup requests
for item in lookup_list:
    if item in phone_book:
        key_name = item.strip()
        value_name = phone_book[item].strip()
        print(key_name, '=', value_name, sep='')
    else:
        print('Not found')
