import pandas as pd
import numpy as np
from itertools import product

from day_2 import get_data
from day_4 import get_columns, create_crossword

def converting_to_integers(cw):
    # all elements in an array (hence in a pd.Series) have to be of same type
    # hence, here we are converting all elements into int64
    cw_readable = cw.copy()

    for i in (range(len(cw))):
        for j in range(len(cw.columns)):
            if cw.iloc[i,j] == '.':
                cw.iloc[i,j] = int(-1)
            elif int(cw.iloc[i,j]) == cw.iloc[i,j]:
                cw.iloc[i,j] = int(cw.iloc[i,j])

    for i in range(len(cw.columns)):
        cw.iloc[:,i] = cw.iloc[:,i].astype(int)

    return cw

def how_many_for_specific_integer(integer, cw): # counting for 0 and for 9
    # checking how many int(0) there are
    coodinates_0 = []
    for i in (range(len(cw))):
        for j in range(len(cw.columns)):
            if (cw.iloc[i,j]) == integer:
                coodinates_0.append(((i,j)))
    return coodinates_0


def get_neighbors(coordinate, integer):
    for _ in range(len(coordinate)):
        a = coordinate - np.array([0,1])
        b = coordinate + np.array([0,1])
        c = coordinate - np.array([1,0])
        d = coordinate + np.array([1,0])
        neigh = [a,b,c,d]

    neigh_final = []
    for i in range(len(neigh)):
        for j in range(len(neigh[i])):
            neigh_final.append(neigh[i][j])

    return neigh_final


def relevant_coordinates(integer, cw):

    coordinate = how_many_for_specific_integer(integer, cw)
    neigh = get_neighbors(coordinate, integer)

    # Only keep relevant coordinates
    k_s = []
    for k in range(len(neigh)):
        i,j = (neigh[k][0], neigh[k][1])
        if i not in range(len(cw)) or j not in range(len(cw.columns)):
            k_s.append(k)

    for k in reversed(k_s):
        neigh.pop(k)
        k = k-1

    if len(neigh) == 2: # to check for 2
        return [neigh]
    else:
        return neigh, coordinate


def comparing_two_coords_to_know_whether_consecutive_integers(coord_one, coord_two):
    consecutives = [
        np.array([0,1]),
        np.array([1,0])
    ]

    for i in consecutives:
        a, b = abs(np.array(coord_one) - np.array(coord_two)) #[0]
        if a == i[0] and b ==i[1]:
            return True

    return False

def get_all_permutations(cw):
    coordinates = {}
    for i in range(10): # because numbers go until 9 (included)
        coordinate = how_many_for_specific_integer(i,cw)
        neigh, coordinate = relevant_coordinates(i, cw)
        coordinates[i] = coordinate

    # Generate all possible combinations
    keys = list(coordinates.keys())
    values = [coordinates[key] for key in keys]

    # Create permutations
    all_permutations = list(product(*values))

    perms = []
    for i in range(len(all_permutations)):
        possible = {
            0: all_permutations[i][0],
            1: all_permutations[i][1],
            2:all_permutations[i][2],
            3:all_permutations[i][3],
            4:all_permutations[i][4],
            5:all_permutations[i][5],
            6:all_permutations[i][6],
            7:all_permutations[i][7],
            8:all_permutations[i][8],
            9:all_permutations[i][9]
        }
        perms.append(possible)

    return perms

def get_chemins_finaux_possibles(cw, perms):
    chemin = {}
    how_many_0 = len(how_many_for_specific_integer(0,cw))

    possibilities = []

    for j in range(len(perms[:])):
        coordinates = perms[j]
        for i in range(9):
            if comparing_two_coords_to_know_whether_consecutive_integers(coordinates[i], coordinates[i+1]):
                chemin[i] = ((coordinates[i]))
                chemin[i+1] = ((coordinates[i+1]))
        if len(chemin)==10:
            possibilities.append(perms[i])


    chemins_finaux = [possibilities[0]]

    for i in range(how_many_0):
        for j in range(len(perms[:])):
            if perms[i] != perms[j]:
                chemins_finaux.append(perms[j])
            if len(chemins_finaux) == how_many_0:
                break

    return chemins_finaux


def get_answer(cw, perms):

    chemin = {}
    how_many_9 = len(how_many_for_specific_integer(9, cw))

    possibilities = []

    # Loop through permutations to find valid ones
    for coordinates in perms:
        chemin.clear()  # Reset chemin for each permutation
        for i in range(9):
            if comparing_two_coords_to_know_whether_consecutive_integers(coordinates[i], coordinates[i + 1]):
                chemin[i] = coordinates[i]
                chemin[i + 1] = coordinates[i + 1]
        if len(chemin) == 10:
            possibilities.append(coordinates)

    # Initialize chemins_finaux with the first possibility
    chemins_finaux = [possibilities[0]]

    # Track seen possibilities based on the last element (coordinates[9])
    seen_last_elements = {possibilities[0][9]}

    # Add unique possibilities to chemins_finaux
    for coordinates in possibilities[1:]:
        if coordinates[9] not in seen_last_elements:
            chemins_finaux.append(coordinates)
            seen_last_elements.add(coordinates[9])

    # Output chemins_finaux
    return (chemins_finaux)


def answer_part1(perms):
    consecutives = [
        np.array([0,1]),
        np.array([1,0])
    ]

    to_drop = []
    for j in range(len(perms)):
        print(f'Permutation {j} ongoing 🔵')
        p = perms[j]
        for i in range(9):
            res1, res2 = np.array(p[i])-np.array(p[i+1])
            if abs(res1) == abs(consecutives[0][0]) and abs(res2) == abs(consecutives[0][1])\
                or abs(res1) == abs(consecutives[1][0]) and abs(res2) == abs(consecutives[1][1]):
                    next
            else :
                to_drop.append(j)
                break
        print(f'Permutation {j} done ✅')

    return len(perms) - len(to_drop)


if __name__ == '__main__':
    lines = get_data('data/example4-day-10.txt')[:-1]
    columns = get_columns(lines)
    char_per_line = len('89010123')
    cw = create_crossword(columns, char_per_line)
    cw = converting_to_integers(cw)
    perms = get_all_permutations(cw)
    print(f'there are {perms} permutations possible overall')
    # print(answer_part1(perms))
