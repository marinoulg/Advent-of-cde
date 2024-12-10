import random
from operator import add, mul
import pandas as pd
import numpy as np

def get_data(path='data/day-7.txt'):
    data = open(path).read()
    data_list = data.replace('\n', 'yyyy').split('yyyy')[:-1]

    new = []
    for i in range(len(data_list)):
        new_list = data_list[i].split(': ')
        new.append(
            (new_list)
                )

    totals = []
    for_calculus = []
    tots = []

    for i in range(len(new)):
        numbers = []
        totals.append(int(new[i][0]))

        my_list = new[i][1].split(' ')
        for j in my_list:
            numbers.append(int(j))
        tots.append([int(new[i][0]), numbers])
        for_calculus.append(numbers)

    totals_df = pd.DataFrame(totals)
    calculus_df = pd.DataFrame(for_calculus)
    df = pd.merge(calculus_df, totals_df, left_index=True, right_index=True)
    df = df.rename(columns={
        '0_x':0,
        '0_y':'final_result'
    })
    return df



def finding_the_score(df, index):
    scores = []
    scoress = {}
    for _ in range(20):
        score = 1
        my_df = pd.DataFrame(df.iloc[index,:].dropna()).T

        for i in range(len(list(my_df.iloc[0,:-1]))):
                # print('\n we are at i=', i)
                ops = (add, mul)
                operation = random.choice(ops)

                # print('operation is', operation, 'of', score, 'with', df.iloc[0,int(i)])

                if operation == add and score == 0:
                    score = 0

                elif operation == mul and score == 0 :
                    score = 1

                score = operation(score, df.iloc[index,int(i)])
                score = int(score)

        # print('score is',score)

        scores.append(score)


    for j in list(set(scores)):
        if j == df.iloc[index,-1]:
            print('yesss')
            scoress[index] = scores

        else:
            scoress[1000000] = scores


    return scoress
