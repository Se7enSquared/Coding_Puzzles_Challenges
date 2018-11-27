# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
# Given an integer N, print 1 - n on the same line

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')
