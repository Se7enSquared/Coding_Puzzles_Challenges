# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to
# deploy one million lights in a 1000x1000 grid.
#
# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the
# ideal lighting configuration.
#
# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at
# 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive
# ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a
# coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
#
# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent
# you in order.
#
# For example:
#
# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning
# on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

import pandas as pd


# Create grid
def create_grid(col, row):
    data = [['[-]' for x in range(col)] for y in range(row)]
    init_grid = pd.DataFrame(data)
    return init_grid

def parse_instructions(line_of_instructions):

    #for each line of instruction:
        #if first_word == "turn":
            # store the next word
            # append word to tuple
        #else #first word not "turn":
            # it's a toggle. Set instruction to toggle
            # append toggle to tuple
        # skip get first number before , store in tuple
        # get first number after , store in tuple
        # get first number after "through", store in tuple
        # get number after second , store in tuple
    return #tuple of (instruction, x1, y1, x2, y2)


# turn off range of lights
def turn_off(df, start_row, start_col, end_row, end_col):
    grid.at[start_col:end_col, start_row:end_row] = '[-]'
    return grid


# turn on range of lights
def turn_on(df, start_row, start_col, end_row, end_col):
    grid.at[start_col:end_col, start_row:end_row] = '[O]'
    return grid


# toggle range of lights
def toggle(df, start_row, start_col, end_row, end_col):
    # need to figure out toggle
    # run a for loop that checks each item in the range
    # if item is - change to 0 and vice-versa
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if df[i][j] == '[O]':
                df[i][j] = '[-]'
            else:
                df[i][j] = '[O]'

    return 0


# instruction caller
def switcher(df, instruction, start_row, start_col, end_row, end_col):
    if instruction == "off":
        turn_off(df, start_row, start_col, end_row, end_col)
    elif instruction == "toggle":
        toggle(df, start_row, start_col, end_row, end_col)
    elif instruction == "on":
        turn_on(df, start_row, start_col, end_row, end_col)


# main
if __name__ == '__main__':
    grid = create_grid(10, 10)
    # sets grid value columns 2:3 at rows 5:8 to *
    turn_on(grid, 2, 5, 3, 8)
    print(grid)

    toggle(grid, 2, 5, 3, 8)
    print(grid)