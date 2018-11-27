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
    data = [['[ ]' for x in range(col)] for y in range(row)]
    init_grid = pd.DataFrame(data)
    return init_grid


# turn off range of lights
def turn_off(df, start_row, start_col, end_row, end_col):
    grid.at[start_col:end_col, start_row:end_row] = '[ ]'
    return grid


# turn on range of lights
def turn_on(df, start_row, start_col, end_row, end_col):
    grid.at[start_col:end_col, start_row:end_row] = '[*]'
    return grid


# toggle range of lights
def toggle(df, start_row, start_col, end_row, end_col):
    # need to figure out toggle
    return 0


# instruction caller
def switcher(df, instruction, start_row, start_col, end_row, end_col):
    if instruction == "turn off":
        turn_off(df, start_row, start_col, end_row, end_col)
    elif instruction == "toggle":
        toggle(df, start_row, start_col, end_row, end_col)
    elif instruction == "turn on":
        turn_on(df, start_row, start_col, end_row, end_col)


# main
if __name__ == '__main__':
    grid = create_grid(10, 10)
    # sets grid value columns 2:3 at rows 5:8 to *
    grid = turn_on(grid, 2, 1, 3, 7)
    print(grid)