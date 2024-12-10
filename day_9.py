import pandas as pd
import numpy as np

def get_data(path='data/day-9.txt'):
    data = open(path, 'r').read()
    data = data.replace('\n', '')
    return data

def get_free_space_and_files(data):
    data_num = []
    for i in data:
        data_num.append(int(i))
    # for data = '12345' --> returns list a-of integers [1, 2, 3, 4, 5]

    free_space = {}
    files = {}
    files[0]=data_num[0]
    for idx in range(len(data_num)):
        if idx%2==0 and idx!=0:
            free_space[idx-1+0.01] = (data_num[idx-1])
        elif idx >0:
            files[idx+1] = (data_num[idx+1])


    free_space_dots = {}
    for i,j in free_space.items():
        free_space_dots[i]=(j*'.')
    free_space_dots

    return free_space_dots, files

def get_new_string(free_space_dots, files):

    # Get a list of tuples (index, nb_of_block_for_file)
    my_list = sorted(files.items())

    for key, value in free_space_dots.items():
        my_list.append((key, value))

    # Put it all in a df
    df = pd.DataFrame(my_list).sort_values(by=0)
    df = df[[1]]
    df = df.reset_index()
    df = df.rename(columns={1:'to_multiply'})
    df

    # Get new_string
    new_string = str() # useless ??
    for idx_df in df.index:
        if isinstance(df.iloc[idx_df, 1], int):
            new_string += (str(df.iloc[idx_df, 0])*df.iloc[idx_df, 1])
        else:
            new_string += (df.iloc[idx_df,1])

    return df, new_string


def get_my_list_not_new_string(df):
    my_array = np.array([])
    for idx_df in df.index:
        if isinstance(df.iloc[idx_df, 1], int):
            array_temp = np.array([int(df.iloc[idx_df, 0])]*df.iloc[idx_df, 1])
            # print(array_temp)
            my_array = np.append(my_array,array_temp)
        else:
            my_array = np.append(my_array,[df.iloc[idx_df,1]])

    my_list = []

    for i in my_array:
        try:
            my_list.append(int(float(i)))
        except ValueError:
            my_list.append((i))

    return my_list



def count_dots(new_string):
    count = 0 # counting number of '.' in my big string
    for i in new_string.replace('.', ' . ').split():
        if i == '.':
            count += 1
    return count


def get_output_list(my_list):
    output_list = []

    for item in my_list:
        if isinstance(item, int):
            output_list.append(item)
        elif isinstance(item, str):
            if item == '.':  # Single dot remains as is
                output_list.append('.')
            else:  # Replace multi-character strings like '...' or '..' with repeated '.'
                output_list.extend(['.'] * len(item))

    # Iterate over the list to "defragment" it
    for idx in range(len(output_list)):
        if output_list[idx] == '.':  # Find the first free space (dot)
            # Look for the last non-dot element in the list
            for target_idx in range(len(output_list) - 1, idx, -1):
                if output_list[target_idx] != '.':  # Found a file block to move
                    # Move the file block to the leftmost dot
                    output_list[idx] = output_list[target_idx]
                    output_list[target_idx] = '.'  # Mark the original spot as free
                    break  # Exit the inner loop after moving one block
    return output_list

def get_answer_part_one(output_list):
    df = pd.DataFrame(output_list)
    df = df.reset_index()

    for idx in df.index:
        if df.iloc[idx, 1]=='.':
            break
    df = df.iloc[:idx]
    return np.sum(df['index']*df[0])







def get_final_string(new_string): # to be modified from here onwards
    count = count_dots(new_string)

    # Know whether to go until range(count) or range(count-1)
    upside_down = []
    for i in range(len(new_string)):
        upside_down.append(new_string[-i])
    string_ups_down = ''.join(upside_down)
    idx_usp_down = string_ups_down.find('.')
    string_ups_down[idx_usp_down:idx_usp_down+2]



    if string_ups_down[idx_usp_down:idx_usp_down+2] == '..':
        for _ in range(count-1):
            idx = new_string.find('.')
            temp_first = new_string[:idx+1]
            temp_second = new_string[idx+1:]
            temp_first = temp_first.replace(temp_first[idx], temp_second[-1])
            temp_second = temp_second[:-1]
            new_string = ''.join((temp_first, temp_second))
            # print(new_string)

        final_result = new_string+(count-1)*'.'

    else :
        for _ in range(count):
            idx = new_string.find('.')
            temp_first = new_string[:idx+1]
            temp_second = new_string[idx+1:]
            temp_first = temp_first.replace(temp_first[idx], temp_second[-1])
            temp_second = temp_second[:-1]
            new_string = ''.join((temp_first, temp_second))
            # print(new_string)

        final_result = new_string+(count)*'.'


    return final_result

def final_result_part_one(final_result):
    final_result = final_result.replace('.', '')

    new_dict = {}

    for idx in range(len(final_result)):
        new_dict[idx] = int(final_result[idx])

    values = np.array(list(new_dict.values()))
    keys = np.array(list(new_dict.keys()))
    df = pd.DataFrame([keys,values]).T
    return np.sum(keys*values)
