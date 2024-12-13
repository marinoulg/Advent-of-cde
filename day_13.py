import pandas as pd
import numpy as np
import sys
import os

from sympy import symbols, Eq, solve
from sympy.core.numbers import Integer

def get_data_into_df(path):
    data = open(path, 'r').read()
    data = data.replace('X+', '').replace('Y+', '').replace('n A', 'n_A').replace('n B', 'n_B').replace('X=', '').replace('Y=', '')
    data = data.split('\n\n')

    data_bis = []
    for i in range(len(data)):
        a = data[i].split('\n')

        bis = []
        for i in range(len(a)):
            bis.append(a[i].split(': '))
        data_bis.append(bis)

    x_y = []
    for j in range(len(data_bis)):
        xx = []
        for i in range(len(data_bis[0])):
            x_y.append(data_bis[j][i][1].split(','))

    df = pd.DataFrame(x_y, columns=['eq1', 'eq2'], index=np.array(['A', 'B', 'sum']*int(len(x_y)/3)))
    return df

def get_tokens_and_most_prices_possible(df):
    solutions = []
    instance = 0
    for i in range((int(df.shape[0]))):
        if i%3==0:
            instance += 1
            df_bis = (df[i:i+3])

            i, j, k = int(df_bis.loc['A','eq1']), int(df_bis.loc['B','eq1']), int(df_bis.loc['sum', 'eq1'])
            l, m, n = int(df_bis.loc['A','eq2']), int(df_bis.loc['B','eq2']), int(df_bis.loc['sum', 'eq2'])

            a, b = symbols('a b')
            eq1 = Eq(a*i + b*j, k)
            eq2 = Eq(a*l + b*m, n)
            solution = solve((eq1,eq2), (a, b))

            if solution[a] < 100 and solution[b] < 100:
                if isinstance(solution[a], Integer) and isinstance(solution[b], Integer):
                    solutions.append((solution, instance))


    tokens = []
    most_prices = []

    for i in range(len(solutions)):
        tokens.append((int(solutions[i][0][a])*3 + int(solutions[i][0][b])*1))
        most_prices.append(solutions[i][1])
    tokens

    most_prices_poss = len(most_prices)
    tokens_min = np.array([tokens]).sum()

    return most_prices_poss, tokens_min

def get_new_df(df):
    for i in range(df.shape[0]-3):
        if i%3==0:
            df.iloc[i+2, 0] = 10000000000000 + int(df.iloc[i+2, 0])
            df.iloc[i+2, 1] = 10000000000000 + int(df.iloc[i+2, 1])

    df.iloc[-1, 0] = 10000000000000 + int(df.iloc[-1, 0])
    df.iloc[-1, 1] = 10000000000000 + int(df.iloc[-1, 1])

    return df

def get_new_tokens_part2(df):
    solutions = []
    instance = 0
    for i in range((int(df.shape[0]))):
        if i%3==0:
            instance += 1
            df_bis = (df[i:i+3])

            i, j, k = int(df_bis.loc['A','eq1']), int(df_bis.loc['B','eq1']), int(df_bis.loc['sum', 'eq1'])
            l, m, n = int(df_bis.loc['A','eq2']), int(df_bis.loc['B','eq2']), int(df_bis.loc['sum', 'eq2'])

            a, b = symbols('a b')
            eq1 = Eq(a*i + b*j, k)
            eq2 = Eq(a*l + b*m, n)
            solution = solve((eq1,eq2), (a, b))

            if isinstance(solution[a], Integer) and isinstance(solution[b], Integer):
                solutions.append((solution, instance))


    tokens = []
    most_prices = []

    for i in range(len(solutions)):
        tokens.append((int(solutions[i][0][a])*3 + int(solutions[i][0][b])*1))
        most_prices.append(solutions[i][1])
    tokens

    most_prices_poss = len(most_prices)
    tokens_min = np.array([tokens]).sum()

    return most_prices, tokens_min
