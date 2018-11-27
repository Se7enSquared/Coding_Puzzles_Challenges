# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
# Read an integer N for all non-negative integers i < N, print i^2

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(pow(i, 2))