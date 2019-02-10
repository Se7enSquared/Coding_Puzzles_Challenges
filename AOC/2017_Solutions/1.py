import nltk

file_content = open('input1.txt').read()
floor = 0
for character in file_content:
    if character == '(':
        floor += 1
    else:
        floor -= 1
print(floor)