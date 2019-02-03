# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
#   Print the hash of a tuple of length n

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))