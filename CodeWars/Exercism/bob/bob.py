def hey(phrase):
    phrase = phrase.strip()
    if not phrase:
        return 'Fine. Be that way!'
    elif phrase.isupper() and phrase.endswith('?'):
        return "Calm down, I know what I'm doing!"
    elif phrase.endswith('?'):
        return 'Sure.'
    elif phrase.isupper():
        return "Whoa, chill out!"
    else:
        return 'Whatever.'
