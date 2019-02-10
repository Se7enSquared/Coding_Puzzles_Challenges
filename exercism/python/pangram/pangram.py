def is_pangram(sentence):
    # if there are non alpha chars in the string, remove them
    if any(not char.isalpha() for char in sentence.lower()):
            sentence = ''.join([i for i in sentence if i.isalpha()])
    # create a set of characters in the sentence
    letters = set(sentence.lower())
    # if the set has 26 characters, it contains every letter
    if len(letters) == 26:
        return True
    return False
