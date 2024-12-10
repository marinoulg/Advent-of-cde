import pandas as pd
import numpy as np

from day_4 import get_lines

def get_data(path):
    data = open(path, 'r').read()
    data = data.split('\n')

    lines = []
    for i in range(len(data)):
        lines.append([data[i]])
    return lines

def get_lists(lines):
    new_lines = []
    for i in range(len(lines)):
        new_lines.append(lines[i][0].replace('\n', ''))

    lists = []
    for i in range(len(new_lines)):
        temp = []
        for j in new_lines[i].split():
            temp.append(int(j))
        lists.append(temp)
    return lists

def get_diff_as_dataframe(lists, length):
    data = pd.DataFrame(lists)
    diff = data.diff(axis=1)
    diff = diff[list(range(1,length))]
    return diff

def get_diff_lists_per_row(diff):
    diff_list = []
    for idx in range(len(diff)):
        mylist = []
        for i in list(diff.iloc[idx,:]):
            if not np.isnan(i):
                mylist.append(i)
        diff_list.append(mylist)
    return diff_list

# Intermediary functions

def ispositive_num(num=0):
    if num:
        if num > 0:
            return True
        else:
            return False


def ispositive(list_of_num=0):
        my_list = []
        for i in list_of_num:
                if ispositive_num(i):
                    my_list.append(True)

        if len(list_of_num) == len(my_list):
            return True
        else:
            return False

def isnegative_num(num=0):
    if num:
        if num < 0:
            return True
        else:
            return False


def isnegative(list_of_num=0):
        my_list = []
        for i in list_of_num:
                if isnegative_num(i):
                    my_list.append(True)

        if len(list_of_num) == len(my_list):
            return True
        else:
            return False

# Back to exercise

def get_safes(diff_list):
    safes = []
    for j in range(len(diff_list)):
        a = diff_list[j]
        possible = {}
        for i in range(len(a)):
            if abs(a[i]) in range(1,4):
                possible[i] = a[i]


        if len(possible) == len(a) and (ispositive(a) or isnegative(a)) and len(a) != 0:
            # print('True')
            safes.append([j, a])

    return safes










def ispositive_except_one(list_of_num):
        b = list_of_num
        mylist = []
        for idx in range(len(b)):
            if ispositive_num(b[idx]):
                mylist.append((True,idx))
            else:
                mylist.append((False,idx))

        count = []
        for i in mylist:
            if i[0] == False:
                count.append(i[1])

        if len(count) == 1:
            # return (i[1]) # returns the index associated with the falty positive
            return count[0]



        # my_list = []
        # for i in list_of_num:
        #         if ispositive_num(i):
        #             my_list.append(True)

        # if len(list_of_num) == len(my_list)+1:
        #     return i



def isnegative_except_one(list_of_num):
        b = list_of_num
        mylist = []
        for idx in range(len(b)):
            if isnegative_num(b[idx]):
                mylist.append((True,idx))
            else:
                mylist.append((False,idx))

        count = []
        for i in mylist:
            if i[0] == False:
                count.append(i[1])

        if len(count)==1:
            return count[0] # returns the index associated with the falty negative


        # my_list = []
        # for i in list_of_num:
        #         if ispositive_num(i):
        #             my_list.append(True)

        # if len(list_of_num) == len(my_list)+1:
        #     return i


def contains_a_zero(list_of_num):
    for i in range(len(list_of_num)):
        if list_of_num[i] == 0:
            return i



def get_potentials(diff_list):
    potentials = []

    for i in range(len(diff_list)):
        b = diff_list[i]
        # print(i)

        if ispositive(b) or isnegative(b):
            pass

        elif ispositive_except_one(b):
            idx = int(ispositive_except_one(b))
            b.pop(idx)

        elif isnegative_except_one(b):
            idx = int(isnegative_except_one(b))
            b.pop(idx)

        elif contains_a_zero(b):
            idx = int(contains_a_zero(b))
            b.pop(idx)


    for i in range(len(diff_list)):
        b = diff_list[i]
        if ispositive(b) or isnegative(b):
            potentials.append(b)

    if potentials[-1] == []:
            potentials.pop() # getting rid of the last empty list

    return potentials



def get_safes_part2(potentials):
    return len(get_safes(potentials))


# --------------------------------------------------




def instanciate_data(path='Advent-of-code.csv'):
    data = pd.read_csv(path,delimiter=';')
    data.head()
    data.index = data['Unnamed: 0']
    data.drop(columns='Unnamed: 0', inplace=True)
    data.reset_index(inplace=True)
    data.drop(columns='Unnamed: 0', inplace=True)
    return data


def df_difference(data, idx_col_0,id7):
    results = []

    for j in range(data.shape[0]):
        interm_results = []

        for i in range(idx_col_0,id7):
            if data.iloc[j,i] < 3+data.iloc[j,i+1]:
                result = (data.iloc[j,i+1] - data.iloc[j,i])
                interm_results.append(result)

        interm_results.append(data.iloc[j,id7] - data.iloc[j,id7-1])

        results.append(interm_results)

    df_differences = pd.DataFrame(results,columns=[f'col{i}_vs_col{i+1}' for i in range(idx_col_0+1,id7+2)])
    return df_differences

def only_inferiors(inferiors):
    # Doesn't consider absolutely no NaN
    for col in inferiors.columns:
        inferiors = inferiors[(inferiors[col] > 0) #| np.isnan(inferiors[col])
                              ]
        for diff,idx in zip(inferiors[col],inferiors.index):
            if abs(diff)>3:
                inferiors.drop(labels=idx, inplace=True)

    return inferiors


def only_superiors(superiors):
    # Doesn't consider absolutely no NaN
    for col in superiors.columns:
        superiors = superiors[(superiors[col] < 0) #| np.isnan(superiors[col])
                              ]

        for diff,idx in zip(superiors[col],superiors.index):
            if abs(diff)>3:
                superiors.drop(labels=idx, inplace=True)

    return superiors

def final(data, idx0=0, idx6=6, col_to_drop='col_8', safes=None):
    data_1 = data.drop(columns=col_to_drop)
    diff = df_difference(data_1, idx0, idx6)

    inferiors_7 = only_inferiors(diff)
    superiors_7 = only_superiors(diff)

    data_inf = data[np.isnan(data[col_to_drop])]
    for idx in data_inf.index:
        if idx not in superiors_7.index:
            data_inf.drop(labels=idx, inplace=True)

    data_sup = data[np.isnan(data[col_to_drop])]
    for idx in data_sup.index:
        if idx not in inferiors_7.index:
            data_sup.drop(labels=idx, inplace=True)

    if col_to_drop!=None:
        safes = pd.concat([safes, data_inf])
    else:
        safes = data_inf

    safes = pd.concat([safes, data_sup])
    return safes
