import pandas as pd
import numpy as np



def get_lines(path='data/input-day-6.txt', char_per_line=130):
    data = open(path, 'r').read()

    lines = []
    idx = char_per_line+1

    for i in range(char_per_line):
        line = data[:idx]
        lines.append([line])
        data = data[idx:]
    return lines


def get_columns_for_crossword(lines, char_per_line):
    columns = []
    for j in range(len(lines)):
        col1 = []
        for i in range(len(lines)):
            col1.append(lines[i][0][j])

        columns.append(col1)
    cw = pd.DataFrame(columns, index=[f'l_{i}' for i in range(char_per_line)]).T
    return cw


def find_go_up(data, cw, char_per_line):
    data = open('data/example-day-6.txt','r').read()
    idx = data.find("^") # ^ is in row 91, element
    which_row = int(idx/char_per_line - 1)
    which_column = ''.join(list(cw.loc[which_row, :].values)).find('^') # returns index 4, aka c_4 is the column
    coordinates = (which_row, which_column)
    return cw, coordinates


def go_up(coordinates, cw):
    which_row = coordinates[0]
    which_column = coordinates[1]
    print(coordinates)
    cw.iloc[coordinates]='X'

    for i in range(which_row):
        if cw.iloc[which_row-i, which_column]=='.':
            cw.iloc[which_row-i, which_column] = 'X'
        if cw.iloc[which_row-i-1, which_column]=='#':
            cw.iloc[which_row-i, which_column] = '>'
            coordinates = (which_row-i, which_column)
            break

    return cw, coordinates


# if '>': # go right until obstacle
def go_right(coord_sign, cw):
    which_row = coord_sign[0]
    which_column = coord_sign[1]

    for i in range(which_column, len(cw.columns)-1):
        if cw.iloc[which_row, i] == '.':
            cw.iloc[which_row, i] = 'X'
        elif cw.iloc[which_row, i] == '#':
            cw.iloc[which_row, i-1] = 'v'
            break

    cw.iloc[coord_sign]='X' # modify the '>' by an 'X' at the end

    coord = (which_row, i)
    # if cw.iloc[coord] =='#':
    #     coord = (coord[0], coord[1]-1)

    # print(which_row, i)
    return cw, coord


def go_down(coord_sign, cw):
    which_row = coord_sign[0]
    which_column = coord_sign[1]

    for i in range(which_row, len(cw)-1):
        # print(i)
        if cw.iloc[i, which_column] == '.':
            cw.iloc[i, which_column] = 'X'

        if cw.iloc[i+1, which_column] == '.':
            cw.iloc[i+1, which_column] = 'X'

        if cw.iloc[i+1, which_column] == '#':
            cw.iloc[i, which_column] = 'v'
            break

    cw.iloc[coord_sign]='X'
    new_coord = (i, which_column)


    return cw, new_coord

def go_left(new_coord, cw):
    which_row = new_coord[0]
    which_column = new_coord[1]

    for i in range(which_column):
        col = which_column-i
        if cw.iloc[which_row, col]=='.':
            cw.iloc[which_row, col]='X'
        if cw.iloc[which_row, col-1]=='#':
            cw.iloc[which_row, col]='^'
            break
    cw.iloc[new_coord]='X'
    new_coord = (which_row, col)

    return cw, new_coord

def count_total(cw):
    counts = []
    for i in range(len(cw)):
        my_list = ''.join(list(cw.iloc[i,:].values)).replace('X', ' X ').split()
        # my_list_deux = ''.join(list(cw.iloc[i,:].values)).replace('^', ' ^ ').split()
        # my_list_trois = ''.join(list(cw.iloc[i,:].values)).replace('>', ' > ').split()
        # my_list_quatre = ''.join(list(cw.iloc[i,:].values)).replace('<', ' < ').split()
        # my_list_cinq = ''.join(list(cw.iloc[i,:].values)).replace('v', ' v ').split()

        count = 0
        for element in my_list:
            if element =='X':
                count += 1
        # for element in my_list_deux:
        #     if element =='^':
        #         count += 1
        # for element in my_list_trois:
        #     if element =='>':
        #         count += 1
        # for element in my_list_quatre:
        #     if element =='<':
        #         count += 1
        # for element in my_list_cinq:
        #     if element =='v':
        #         count += 1
        counts.append(count)

    return pd.Series(counts).sum()
