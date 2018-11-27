# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.
#
# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
#
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?


# return true if at least 3 vowels are found in the string
def has_3_vowels(s):
    vowel_list = ('a', 'e', 'i', 'o', 'u')
    vowels = 0
    for char in s:
        if char in vowel_list:
            vowels += 1
        if vowels >= 3:
            return True
    if vowels < 3:
        return False

def has_double_letter(string):
    prev = ''
    for letter in string:
        if letter == prev:
            return True
        prev = letter
    return False

# FAILURE POINT
def has_naughty(s):
    if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
        return True
    return False

def naughty_nice(filename):
    count_of_nice_strings = 0
    with open(filename) as file:
        for string in file:
            print(string)
            if not has_3_vowels(string):
                print(string, ' does not have 3 vowels ')
                continue
            print(string, ' has 3 vowels ')
            if not has_double_letter(string):
                print(string, ' does not have a double letter ')
                continue
            print(string, ' has double letter ')
            if has_naughty(string):
                print(string, ' has a naughty string ')
                continue
            print(string, ' has no naughty strings ')
            print(string, ' is nice!! ')
            count_of_nice_strings += 1
            print(count_of_nice_strings, " nice")
    print(count_of_nice_strings)

if __name__ == '__main__':
    naughty_nice('C:\\scripts\\advent\\2015_AOC_day5_input.txt')