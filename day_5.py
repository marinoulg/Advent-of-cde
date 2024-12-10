import pandas as pd
import numpy as np


def get_lines(path='data/day-5.txt', char_per_line=5, length=1176):
    data = open(path, 'r').read()

    lines = []
    idx = char_per_line+1

    for i in range(length):
        line = data[:idx]
        lines.append([line])
        data = data[idx:]

    line_lists = []
    for i in range(len(lines)):
        line_list = lines[i][0].replace('\n','').split('|')
        line_lists.append(
            [int(line_list[0]), int(line_list[1])]
            )

    return line_lists


def get_df(lines):
    df = pd.DataFrame(lines, columns=['first_value', 'sec_value'])
    return df


def order_of_modif(df):
    # Goal of this is to find which numbers are to be modified secondly after
    # their first modification to be made

    my_dict = {}
    for num in df['first_value'].unique():
        my_dict[int(num)] = list((df[df['first_value']==num]['sec_value']))
    return my_dict


def get_page_ordering_rules(path='data/day-5-part2.txt'):
    data_bis = open(path, 'r').read()
    my_list = data_bis.replace('\n', ' ').split()

    page_ordering_rule = []
    for i in range(len(my_list)):
        integers = []
        for num in my_list[i].split(','):
            integers.append(int(num))

        page_ordering_rule.append(integers)

    return page_ordering_rule

def get_real_orders(page_ordering_rule, my_dict):
    # Goal of this cell is to find, for each number in a given sequence of ordered pages,
    # which of its other numbers are not present in the list of numbers to be modified
    # after said number (this list being my_dict[num])

    results = []

    for idx in range(len(page_ordering_rule)):
        page = page_ordering_rule[idx]
        tots_not = {}

        for current_page in page:
            not_in = [num for num in page if num not in my_dict.get(current_page, [])]
            tots_not[current_page] = not_in

        totals = []
        for key, value in tots_not.items():
            totals.append([key, value])

        # Finding if 1 given line is in the correct order
        # if result = [False] or with many False, it is False
        # else, it is True

        result = []
        for i in range(len(pd.DataFrame(totals)[1])-1):
            if len(pd.DataFrame(totals)[1][i]) > len(pd.DataFrame(totals)[1][i+1]):
                result.append(False)
        if result == []:
            results.append(page_ordering_rule[idx])

    return results

def get_final_result(results):
    # Once we have a list of true_orders, we get the middle value for each

    middles = []
    for i in range(len(results)):
        middle = int(len(results[i])/2)
        # print(middle)
        middles.append(results[i][middle])

    final_result = pd.Series(middles).sum()
    return final_result

def get_false_order(page_ordering_rule, my_dict, idx):
    # Goal of this cell is to find, for each number in a given sequence of ordered pages,
    # which of its other numbers are not present in the list of numbers to be modified
    # after said number (this list being my_dict[num])
    results = []
    page = page_ordering_rule[idx]
    tots_not = {}

    for current_page in page:
        not_in = [num for num in page if num not in my_dict.get(current_page, [])]
        tots_not[current_page] = not_in

    totals = []
    for key, value in tots_not.items():
        totals.append([key, value])

    # Finding if 1 given line is in the correct order
    # if result = [False] or with many False, it is False
    # else, it is True
    result = []
    for i in range(len(pd.DataFrame(totals)[1])-1):
        if len(pd.DataFrame(totals)[1][i]) > len(pd.DataFrame(totals)[1][i+1]):
            result.append(False)
    if result != []:
        results.append(page_ordering_rule[idx])

    return totals, results

def reorganize_false_orders(totals):
    # Sort the input data based on the length of the sublists in ascending order
    sorted_data = sorted(totals, key=lambda x: len(x[1]))

    # Extract the first number from each sorted sublist
    result = [item[0] for item in sorted_data]

    return result

def get_list_all_false_reorganized_orders(page_ordering_rule, my_dict):
    results = []

    for i in range(len(page_ordering_rule)):
        total, result = get_false_order(page_ordering_rule, my_dict, idx=i)
        # if reorganize_false_orders(total)!=result:
        #     print('result vs real result')
        #     print(result)
        #     print(reorganize_false_orders(total))
        if result != []:
            results.append(reorganize_false_orders(total))
    return results
