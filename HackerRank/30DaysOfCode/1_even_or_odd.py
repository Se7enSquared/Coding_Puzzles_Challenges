# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
#   Given an integer, , perform the following conditional actions:
#   If  is odd, print Weird
#   If  is even and in the inclusive range of  to , print Not Weird
#   If  is even and in the inclusive range of  to , print Weird
#   If  is even and greater than , print Not Weird

def weird():
    print('Weird')


def not_weird():
    print('Not Weird')

if __name__ == '__main__':
    n = int(input())

    if n % 2 == 0:
        if n >= 2 and n <= 5:
            not_weird()
        elif n >= 6 and n <= 20:
            weird()
        elif n > 20:
            not_weird()
    else:
        weird()