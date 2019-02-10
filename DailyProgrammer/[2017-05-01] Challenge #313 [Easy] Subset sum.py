#   date : 5/4/2017
#   author : H. Gray
#   email : 7squared@zoho.com
#
#   title : Heather Gray
#   brief : return true if two integers in a given list add to zero
#
#   source : Daily Programmer
#   https://www.reddit.com/r/dailyprogrammer/comments/68oda5
#   /20170501_challenge_313_easy_subset_sum/

#   Description
#
#   Given a sorted list of distinct integers, write a function that returns
#   whether there are two integers in the list that add up to 0. For example,
#   you would return true if both -14435 and 14435 are in the list, because
#   -14435 + 14435 = 0. Also return true if 0 appears in the list.
#
#   Examples
#
#   [1, 2, 3] -> false
#   [-5, -3, -1, 2, 4, 6] -> false
#   [] -> false
#   [-1, 1] -> true
#   [-97364, -71561, -69336, 19675, 71561, 97863] -> true
#   [-53974, -39140, -36561, -23935, -15680, 0] -> true

def subset_sum(list_of_numbers):

    # list to hold nums that add to zero
    zero_sum = []
    # list of nums converted to string
    string_list = []

    # convert list to list of stings
    for i in range(0, len(list_of_numbers)):
        string_list.append(str(list_of_numbers[i]))

    # iterate through list and compare numbers
    for i in range(0, len(list_of_numbers)-1):

        current_number = list_of_numbers[i]
        # if number is not negative
        if current_number > 0:
            # add a negative sign for the comparison
            number_to_compare = '-' + str(list_of_numbers[i])
            # look for number in the list
            if number_to_compare in string_list:
                zero_sum.append(list_of_numbers[i])
        # if number is negative
        elif current_number < 0:
            # make it not negative
            current_number = list_of_numbers[i] * -1
            # look for it in the list of strings
            if str(current_number) in string_list:
                zero_sum.append(list_of_numbers[i])

    # return all numbers that add to zero
    return zero_sum

list_of_nums = [-100, 100, -3, 3, 2, 4, 1, 8, -2]
print(subset_sum(list_of_nums))