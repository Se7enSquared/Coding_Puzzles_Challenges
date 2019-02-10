def is_isogram(word):
    for i in range(0, len(word)):
        letter = word[i].lower()
        if letter.isalpha():
            if letter in word[i+1:]:
        	    return False
    return True
