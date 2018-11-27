flash = ['3', 'K', '5', 'A', '5', '6', '7', 'J', '7', '9', '10', 'Q', 'Q', '6', '8', '7', '4', 'J', '8', '9', 'K', 'J',
         '10', '4', 'K', '4']
turtle = ['2', '8', '9', 'Q', 'A', 'K', '6', '3', 'J', '2', '4', '3', '3', '8', 'A', '2', '6', '7', '9', '10', 'A', '5',
          'Q', '10', '2', '5']


def snap(flash_pile, turtle_pile):
    mid_pile = []
    ohsnap = 0
    # 0 = Flash & 1 = Turtle
    x = [1, 0]
    players = {0: 'Flash', 1: 'Turtle'}

    toggle = 0
    for i in range(len(turtle_pile)):
        # if it's the beginning of new game, set player to Flash
        if i == 0:
            print("A new game is starting!")
            toggle = 0
            ohsnap = 0
            print("Toggle starts at ", toggle)
            print("# snaps starts at ", ohsnap)
        print("It's", players[toggle], "'s turn")
        if len(mid_pile) == 0:
            print("The mid_pile is empty")
            mid_pile.append(flash_pile.pop(0))
            # set player to turtle
            toggle = x[toggle]
            print("First item added to mid_pile: ", mid_pile)
        if toggle == 0:
            play = flash_pile.pop(0)
            ("Flash plays: ", play)
            if play == mid_pile[-1]:
                print(play, " = ", mid_pile[-1])
                ohsnap += 1
                flash_pile += mid_pile
                continue
            mid_pile.append(play)
            print("appended", play,"to mid_pile : ", mid_pile)
            toggle = x[toggle]
            print("toggled to: ", players[toggle])
        else:
            play = turtle_pile.pop(0)
            ("Turtle plays: ", play)
            if play == mid_pile[-1]:
                print(play, " = ", mid_pile[-1])
                ohsnap += 1
                flash_pile += mid_pile
                continue
            mid_pile.append(play)
            print("appended", play, "to mid_pile : ", mid_pile)
            toggle = x[toggle]
            print("toggled to: ", players[toggle])


    # IS CARD CURRENTLY BEING PLAYED = LAST CARD ON THE LIST
    return ohsnap


print(snap(flash, turtle))
