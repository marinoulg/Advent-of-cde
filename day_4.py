import pandas as pd
import numpy as np



def get_lines(path='data/day-4.txt', char_per_line=140):
    data = open(path, 'r').read()

    lines = []
    idx = char_per_line+1

    for i in range(char_per_line):
        line = data[:idx]
        lines.append([line])
        data = data[idx:]
    return lines


def count_XMAS_per_line(lines):
    total_count =[]

    for i in range(len(lines)):
            # Pour la 1ere ligne, j'ai x fois le mot 'XMAS'
            l1 = lines[i][0]

            l1_b = l1.replace('XMAS', ' OOOO ')
            l1_b.split()

            count = 0
            for i in l1_b.split():
                if i == 'OOOO':
                    count += 1

            # Pour la 1ere ligne, j'ai x fois le mot 'SAMX'
            l1_bis = l1.replace('SAMX', ' SAMX ')
            l1_bis.split()

            for i in l1_bis.split():
                if i == 'SAMX':
                    count += 1

            total_count.append(count)
    return pd.Series(total_count).sum()


def get_columns(lines):
    columns = []
    for j in range(len(lines)):
        col1 = []
        for i in range(len(lines)):
            col1.append(lines[i][0][j])

        columns.append(col1)
    return columns


def create_crossword(columns, char_per_line=140):
    crossword = pd.DataFrame(columns, index=[f'{i}' for i in range(char_per_line)]).T # ATTENTION IT NEEDS TO BE TRANSPOSED TO BE CORRECT
    return crossword


def count_XMAS_per_column(columns):
    total_count_col =[]

    for i in range(len(columns)):
            # Pour la 1ere ligne, j'ai x fois le mot 'XMAS'
            col = ''.join(columns[i])
            col_1 = col.replace('XMAS', ' OOOO ')

            count = 0
            for i in col_1.split():
                if i == 'OOOO':
                    count += 1

            # Pour la 1ere ligne, j'ai x fois le mot 'SAMX'
            col_bis = col.replace('SAMX', ' SAMX ')
            col_bis.split()

            for i in col_bis.split():
                if i == 'SAMX':
                    count += 1

            total_count_col.append(count)

    return pd.Series(total_count_col).sum()


def diagonals_backslash(crossword, char_per_line=140):
    """
    diagonals_slash means in the form of a \
    """

    # # Big to small
    diagonals = []

    for j in range(char_per_line):
        diag = str()
        for i in range(char_per_line-j):
            diag += crossword.loc[f'l_{i}', i+j]
        diagonals.append(diag)

    # Small to big

    for diag_length in range(1, char_per_line):  # all except last one
        diag = ''.join(crossword.iloc[char_per_line-1 - (diag_length - i - 1), i] for i in range(diag_length))
        diagonals.append(diag)

    return diagonals


def count_backslash(diagonals):
    count_diags = []
    for i in diagonals:
        n = i.replace('XMAS', ' OOOO ').split()
        count = 0
        for i in n:
            if i == 'OOOO':
                count += 1
        n_bis = i.replace('SAMX', ' SAMX ').split()
        for i in n_bis:
            if i == 'SAMX':
                count += 1
        count_diags.append(count)

    return pd.Series(count_diags).sum()


def diagonals_slash(crossword, char_per_line=140):

    # Small to big, left to right
    diags = []

    for diag_length in range(1, char_per_line+1):  # 1-based range for clarity
        # Create the current diagonal
        diag = ''.join(crossword.iloc[diag_length - i - 1, i] for i in range(diag_length))
        diags.append(diag)

    # ----------------------------

    # Generate diagonals in reverse order
    # Small to big, right to left
    for diag_length in range(1, char_per_line+1):  # 1 to 140 (inclusive)
        # Create the current diagonal
        diag = ''.join(crossword.iloc[char_per_line-1 - i, char_per_line-1 - (diag_length - i - 1)] for i in range(diag_length))
        diags.append(diag)

    diags = diags[:-1] # we don't consider the middle and biggest diagonal twice
    return diags


def count_diagonals_slash(diags):
    count_diags = []


    for i in diags:
        n = i.replace('XMAS', ' OOOO ').split()
        count = 0
        for i in n:
            if i == 'OOOO':
                count += 1
        n_bis = i.replace('SAMX', ' SAMX ').split()
        for i in n_bis:
            if i == 'SAMX':
                count += 1
        count_diags.append(count)

    return pd.Series(count_diags).sum()
