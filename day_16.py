import pandas as pd
import numpy as np

def get_cw(data):
    cw = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            temp.append(data[i][j])
        cw.append(temp)
    cw = pd.DataFrame(cw)
    clean = cw[(cw=='.') | (cw=='E') | (cw=='S')]
    return cw, clean



def find_start_or_end(to_find, cw):
    for i in range(len(cw)):
        for j in range(len(cw.columns)):
            if cw.iloc[i, j] == to_find:
                return (i,j)


# Dealing with possible columns to know max points
# for col in range(len(cw.columns)):

def count_columns(clean):
    counts_column = {}
    traps = {}
    for col in range(len(clean.columns)-1):

        not_poss = []
        count = 0

        for i in reversed(range(1,len(clean)-1)):
            if pd.isna(clean.iloc[i-1, col]) and pd.isna(clean.iloc[i+1, col]) and clean.iloc[i, col] == '.':
                not_poss.append(i)
                # i+=2
                # print('a')
                continue
            elif pd.isna(clean.iloc[i-1, col]) and pd.isna(clean.iloc[i, col+1]) and pd.isna(clean.iloc[i, col-1]) and clean.iloc[i, col] == '.':
                not_poss.append(i)
                # i+=2
                # print('b')
                continue
            if i-1 in not_poss and pd.isna(clean.iloc[col-1,i]) and pd.isna(clean.iloc[col-1,i]) and clean.iloc[i, col] == '.':
                not_poss.append(i)
                # print('c')
                continue

        for i in (range(1,len(clean)-1)):
            if i-1 in not_poss and pd.isna(clean.iloc[col-1,i]) and pd.isna(clean.iloc[col-1,i]) and clean.iloc[i, col] == '.':
                not_poss.append(i)
                # print('d')
                continue

        for i in reversed(range(1,len(clean))):
            if i not in not_poss and clean.iloc[i, col]=='.':
                    count += 1
            else:
                continue

        counts_column[col] = count
        traps[col] = not_poss

    max_col_score = np.array(list(counts_column.values())).sum()
    return max_col_score, traps



def count_rows(clean):
    counts_column = {}
    traps = {}

    for row in range(len(clean.columns)-1):
        not_poss = []
        count = 0

        for i in reversed(range(len(clean.columns)-1)):
            if pd.isna(clean.iloc[row,i-1]) and pd.isna(clean.iloc[row,i+1]):
                not_poss.append(i)
                continue

            elif pd.isna(clean.iloc[row,i+1]) and pd.isna(clean.iloc[row-1,i]) and pd.isna(clean.iloc[row+1,i]):
                not_poss.append(i)
                continue

            elif i+1 in not_poss and pd.isna(clean.iloc[row-1,i]) and pd.isna(clean.iloc[row+1,i]):
                not_poss.append(i)
                continue


        for i in (range(1,len(clean.columns))):
            if i not in not_poss and clean.iloc[row, i]=='.':
                    count += 1
            else:
                continue

        counts_column[row] = count
        traps[row] = not_poss

    max_row_score = np.array(list(counts_column.values())).sum()
    return max_row_score, traps
