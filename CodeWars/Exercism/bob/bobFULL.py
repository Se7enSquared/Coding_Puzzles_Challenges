def saying_nothing(phrase):
    return not phrase


def asking_question(phrase):
    return phrase.endswith('?')


def yelling(phrase):
    return phrase.isupper()


def yelling_question(phrase):
    return yelling(phrase) and asking_question(phrase)


def hey(phrase):
    phrase = phrase.strip()
    if saying_nothing(phrase):
        return 'Fine. Be that way!'
    elif yelling_question(phrase):
        return "Calm down, I know what I'm doing!"
    elif asking_question(phrase):
        return 'Sure.'
    elif yelling(phrase):
        return "Whoa, chill out!"
    else:
        return 'Whatever.'

def hey(phrase):
    phrase = phrase.strip()
    if saying_nothing(phrase):
        return 'Fine. Be that way!'
    elif yelling_question(phrase):
        return "Calm down, I know what I'm doing!"
    elif asking_question(phrase):
        return 'Sure.'
    elif yelling(phrase):
        return "Whoa, chill out!"
    else:
        return 'Whatever.'

