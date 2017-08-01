# Author's note: the break statements are bad and the double-loop is not
# necessary. Fix in the future

# Author: Heather Gray
# Site: Hackerrank
# Language: Python
# Problem statement:
#   Given a list of commands and data, perform the specified list operation
#   Input example:
#       4 # number of commands that follow
#       insert 0 1 # insert 1 at index 0
#       sort # sort the list
#       print # print the list
#       etc...

if __name__ == '__main__':
    N = int(input())
    list_of_commands = []
    the_output_list = []

    for i in range(N):
        line = input()
        list_of_commands.append(line.split(' '))

    for item in list_of_commands:
        if item[0][0].lower() == 'insert':
            the_output_list.insert(int(item[0][1]), int(item[0][2]))
            break
        elif item[0][0].lower() == 'append':
            the_output_list.append(int(item[0][1]))
            break
        elif item[0][0].lower() == 'remove':
            the_output_list.remove(int(item[0][1]))
            break
        if item[0][0].lower() == 'sort':
            the_output_list.sort()
            break
        elif item[0].lower() == 'pop':
            the_output_list.pop()
            break
        elif item[0][0].lower() == 'reverse':
            the_output_list.reverse()
        elif item[0][0].lower() == 'print':
            print(the_output_list)
            break
