def replace_all(the_string, diction):
    for key in diction:
        the_string = the_string.replace(key, diction[key])
    return the_string


encoded_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

replacement_dict = {'"': ' ', '{': 'a', '|': 'b', ')': "'", '0': '.'}

test_string = replace_all(encoded_string, replacement_dict)

new_string = ''
for word in encoded_string:
    for char in word:
        new_string += chr(ord(char)+2)

another = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")


print(replace_all(new_string, replacement_dict))

print("map".translate(another))

