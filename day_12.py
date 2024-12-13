import numpy as np
import pandas as pd





def get_columns(data):
    columns = []
    for j in range(len(data)):
            col1 = []
            for i in range(len(data)):
                col1.append(data[i][j])

            columns.append(col1)
    return columns


def list_difft_chars(cw):
    # list different char
    cw.iloc[0, :].unique()
    (cw.iloc[1, :].unique())

    difft_char = []
    for i in range(len(cw)):
        if len(cw.iloc[i, :].unique()) == 1:
            difft_char.append(''.join(cw.iloc[i, :].unique()))
        else:
            for j in cw.iloc[i, :].unique():
                difft_char.append(j)

    difft_char = list(set(difft_char))
    return difft_char


def coord_char(cw, i, j, char='A'):
    if cw.iloc[i,j] == char:
        i = i+1
        return (i,j)


def get_coordonate_char(cw, char):
    coord = []
    for i in range(len(cw.columns)):
        for j in range(len(cw)):
            if coord_char(cw, i, j, char):
                coord.append((i,j))
    return coord

def get_dict_coords_all_chars(cw, difft_char):
    my_dict = {}
    for char in difft_char:
        my_dict[char] = get_coordonate_char(cw, char)

    return my_dict



def get_perimeter_and_area(cw, char):
    print(char)
    c = get_coordonate_char(cw, char)
    # print(c)

    longueur = 0
    long = []
    largeur = 0
    larg = []

    for i in range(0,len(c)-1):
        if (c[i][0]) == c[i+1][0]:
            if (c[i][0]) not in long and (c[i][0])!=(c[i+1][0]):
                long.append(c[i][0])
                long.append(c[i+1][0])
            else:
                long.append(c[i+1][0])
        else :
            long.append(c[i][0])
            long.append(c[i+1][0])
        # longueur += 1

    for j in range(len(c)-1):
        if (c[j][1])+1 == c[j+1][1]:
            if (c[j][1]) not in larg and (c[j][1])!=(c[j][1])+1:
                larg.append(c[i][1])
                larg.append(c[i+1][1])
            else:
                larg.append(c[j+1][1])
        else:
            larg.append(c[j][1])
            larg.append(c[j+1][1])

            # largeur += 1


    if long != [] or larg != []:
        if len(pd.Series(long).unique()) == 1:
            longueur = len(long) + 1
            largeur = 1
        elif len(pd.Series(larg).unique()) == 1:
            largeur = len(larg) + 1
            longueur = 1


        elif len(pd.Series(long).unique()) > len(c)/2:
            longueur = len(pd.Series(long).unique()) - 1
            largeur = len(pd.Series(larg).unique())

            perimeter = (longueur+1 + largeur)*2
            area = longueur * largeur
            print('longueur is', longueur)
            print('largeur is', largeur)
            return perimeter, area

        elif len(pd.Series(larg).unique()) > len(c)/2:
            largeur = len(pd.Series(larg).unique()) - 1
            longueur = len(pd.Series(long).unique())

            perimeter = (longueur+1 + largeur)*2
            area = longueur * largeur
            print('longueur is', longueur)
            print('largeur is', largeur)
            return perimeter, area


        else:
            longueur = len(pd.Series(long).unique())
            largeur = len(pd.Series(larg).unique())

    elif long == [] and larg == []:
        longueur = 1
        largeur = 1


    perimeter = (longueur + largeur)*2
    area = longueur * largeur

    # print('long is ', long)
    # print('larg is ', larg)

    print('longueur is', longueur)
    print('largeur is', largeur)

    return perimeter, area
