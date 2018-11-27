flash_pile = ['1', '2', 'a', 'b']
turtle_pile = ['2', '1', 'a', 'c']


def mid_pile_is_empty(mid_pile):
    return len(mid_pile) == 0


def play_card(pile, ohsnap, mid_pile):
    play = pile.pop(0)
    if is_snap(play, mid_pile):
        return ohsnap + 1


def is_snap(play, mid_pile):
    return mid_pile[-1] == play


def get_play(pile):
    play = pile.pop(0)
    return play


def snap(flash_pile, turtle_pile):
    mid_pile = []
    x = [1, 0]
    toggle = 0
    toggle = x[toggle]
    players = {0: 'turtle', 1: 'flash'}
    ohsnap = 0

    # Because turtle always loses, use length of his pile
    for i in range(len(turtle_pile)):
        if toggle == 0:
            play_card(flash_pile, ohsnap, mid_pile)
        else:
            play_card(turtle_pile, ohsnap, mid_pile)
        if mid_pile_is_empty(mid_pile):
            mid_pile.append(get_play())


print(snap(flash_pile, turtle_pile))
