import re

def hey(phrase):
    if phrase.isupper():
    	return 'Whoa, chill out!'
    elif phrase.endswith('?'):
    	return 'Sure.'
    # elif phrase.isspace() or phrase == '' and re.search(r"(\S*)\s*(\S*)", phrase) == '':
    elif all(x.isalpha() or x.isspace() for x in phrase):
    	return 'Fine. Be that way!'
    else:
    	return 'Whatever.'