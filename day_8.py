import pandas as pd
import numpy as np

from day_4 import get_lines, create_crossword, get_columns



def get_crossword(path, char_per_line):
    lines = get_lines(path, char_per_line)
    columns = get_columns(lines)
    cw = create_crossword(columns, char_per_line)
    return cw

def get_possibilities_char(cw):
    possibilities_char = []
    for i in range(len(cw)):
        possibilities_char.append(list(cw.iloc[i,:].unique()))

    my_list = list(set(str(possibilities_char).replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace("'", '').replace(' ', '').split(',')))
    my_list.remove('.')
    return my_list


def get_coordinates_char(char, cw):
    zeros_coord = []
    for i in range(len(cw)):
        for j in range(len(cw)):
            if cw.iloc[i,j] == (char):
                zeros_coord.append(np.array([i,j]))

    return zeros_coord

def coordinates_hastag_for_char(char, zeros_coord, cw):
    hashtags_zeros = []

    for j in range(len(zeros_coord)):
        for i in range(len(zeros_coord)):
            ans_temp = zeros_coord[j] - zeros_coord[i]
            coord_1 = zeros_coord[j] + ans_temp
            coord_2 = zeros_coord[i] - ans_temp

            if list(coord_1) != list(coord_2) \
                and (coord_1[0] in range(0,len(cw.columns)) and coord_1[1] in range(0,len(cw))):
                hashtags_zeros.append(tuple(coord_1))

            elif list(coord_1) != list(coord_2) \
                and (coord_2[0] in range(0,len(cw.columns)) and coord_2[1] in range(0,len(cw))):
                hashtags_zeros.append(tuple(coord_2))


    return list(set(hashtags_zeros))

def merging_cat1_and_cat2_coords(cat1, cat2):
    all_hashtags_coords = cat1.copy()
    for i in cat2:
        all_hashtags_coords.append(i)

    return (list(set(all_hashtags_coords)))


def get_final_resut(possibilities_char, cw):
    cat2 = list()

    for char in possibilities_char:
        coords = get_coordinates_char(char, cw)
        hashtags_char = coordinates_hastag_for_char(char, coords, cw)
        cat2 = merging_cat1_and_cat2_coords(hashtags_char, cat2)

    # final_result = len(cat2)
    result = cat2
    return result

def graph_hastags(cw, result):
    # not using it
    for i in result:
        if cw.iloc[i]=='.':
            cw.iloc[i]='#'
    return cw
