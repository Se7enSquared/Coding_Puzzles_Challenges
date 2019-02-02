# !/bin/python3

# ==============================================================================
#   date : 8/22/2018
#   author : H. Gray
#   email : heathergray153@gmail.com
#
#   title : Hackerrank 30 days of code, day 12: 2D Array
#   brief : Given a 6x6 2D array A, find the sum of each hour glass subset. An
#           hourglass is defined as a subset of A:
#           1 1 1
#             1
#           1 1 1
#           Calculate the hourglass sum for every hourglass in A, then print the
#           maximum hourglass sum.
#
#   source : https://www.hackerrank.com/challenges/30-2d-arrays/problem
# ==============================================================================


# sample array - expected result = 19
arr = [
       [1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]
       ]

# set the starting max sum to a very low negative number to handle cases of
# arrays with negative values
max_sum = -10000000
the_sum = 0

if __name__ == '__main__':

    for row in range(1, 5):
        middle = 1
        for col in range(1, 5):
            the_sum += sum(arr[row - 1][col - 1: col + 2])
            the_sum += arr[row][middle]
            middle += 1
            the_sum += sum(arr[row + 1][col - 1: col + 2])
            if the_sum > max_sum:
                max_sum = the_sum
            the_sum = 0
    print(max_sum)
