import re

def word_count(sentence):
    new_sentence = re.sub(r'[\W_\\]', ' ', sentence)
    new_sentence = new_sentence.lower()
    list_of_words = new_sentence.split()

    word_dict = {}
    
    for word in list_of_words:
    	if word not in word_dict:
    		word_dict[word] = list_of_words.count(word)

    return word_dict