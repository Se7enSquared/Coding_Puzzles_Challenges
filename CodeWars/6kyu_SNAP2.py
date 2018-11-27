flash_pile = ['1', '2', 'a', 'b']
turtle_pile = ['2', '1', 'a', 'c']

mid_pile = []
x = [1, 0]
toggle = 0
toggle = x[toggle]
players = {0: 'turtle', 1: 'flash'}
ohsnap = 0


def mid_pile_is_empty(mid_pile):
    return (mid_pile) == 0


for i in range(len(turtle_pile)):
    # if there's nothing in the pile, it's flash's turn since he always goes first
    if toggle == 0:
        # flash turn
        play = flash_pile.pop(0)
        if mid_pile_is_empty(mid_pile):
            mid_pile.append(play)
            toggle = x[toggle]
            continue
        else:
            if mid_pile[-1] == play:
                ohsnap += 1
                print("SNAP!")
                flash_pile += mid_pile
                mid_pile = []
                continue
    else:
        play = turtle_pile.pop(0)
        if mid_pile_is_empty(mid_pile):
            mid_pile.append(play)
            toggle = x[toggle]
            continue
        else:
            if mid_pile[-1] == play:
                ohsnap += 1
                print("SNAP!")
                flash_pile += mid_pile
                mid_pile = []
                continue
print(ohsnap)
