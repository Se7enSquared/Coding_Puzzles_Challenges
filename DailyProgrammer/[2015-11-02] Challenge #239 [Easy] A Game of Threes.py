# Generate a large number. If that number is divisible by 3, divide by 3.
# Else, add 1 and try again. Continue until the number reaches zero.

from random import randint


def reduce_number(current_number, i):
    i += 1
    if current_number == 1:
        print("The number has been successfully reduced to 1 in ", i,
              " iterations!")
        return
    elif current_number % 3 == 0:
        new_number = current_number / 3
        print("number was divisible by 3. The new number is: ", int(new_number))

    else:
        new_number = current_number + 1
        print(current_number, " not divisible by 3. New number is ",
              int(new_number))

    reduce_number(new_number, i)


# Generate a random number > 100
starting_number = randint(100, 9999)

print("The starting number is: ", starting_number)
reduce_number(starting_number, 0)
