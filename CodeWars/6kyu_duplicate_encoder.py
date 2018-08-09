# Name: Heather Gray
# Date: 8/9/2018
# Kata Level: 6 Kyu
#
# Description:
# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that
# character appears only once in the original string, or ')' if that character appears more than once in the original
# string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples:
#
# "din" => "((("
#
# "recede" => "()()()"
#
# "Success" => ")())())"
#
# "(( @" => "))(("


def duplicate_encode(word):
    new_string = ''
    string_dict = {}

    for letter in word:
        letter_count = word.count(letter.lower())
        string_dict[letter.lower()] = letter_count
        print(string_dict)

    for letter in word:
        if string_dict[letter.lower()] > 1:
            new_string += ')'
        else:
            new_string += '('

    return new_string
