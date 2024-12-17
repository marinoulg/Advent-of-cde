import pandas as pd
import numpy as np

def get_data(path):
    data = open(path, 'r').read()
    data = data.replace('p=', '').replace('v=', '').replace(' ', ',').split('\n')

    data_bis = []

    for j in range(len(data)-1):
        bis = []
        for i in data[j].split(','):
            bis.append(int(i))
        data_bis.append(bis)

    return data_bis

def get_df_robot(data_bis):
    df_robot = pd.DataFrame(data_bis,
             columns=['p_x', 'p_y', 'v_x', 'v_y'],
             index=[f'robot_{i}' for i in range(len(data_bis))] )

    return df_robot

def get_clean_df(len_x, len_y):
    array = []
    for _ in range(len_x):
        array.append(np.array(['.']*len_y))

    basics = pd.DataFrame(array)
    return basics

def coordinates_robots(df_robot):
    robot_coords_arrays = []

    for i in range(len(df_robot)):
        robot_coords_arrays.append(np.array([df_robot.iloc[i, 1], df_robot.iloc[i, 0]]))

    return robot_coords_arrays

def coordinates_velocities(df_robot):
    velocities_arrays = []

    for i in range(len(df_robot)):
        velocities_arrays.append(np.array([df_robot.iloc[i, 3], df_robot.iloc[i, 2]]))

    return velocities_arrays

def visualize_robots_initial(robot_coords_arrays, basics):
    for i in range(len(robot_coords_arrays)):
        if basics.iloc[tuple(robot_coords_arrays[i])] == '.':
            basics.iloc[tuple(robot_coords_arrays[i])] = 1
        else:
            basics.iloc[tuple(robot_coords_arrays[i])] += 1
    return basics

def after_1_sec(robots_position, velocities_arrays, len_x, len_y):
    first_sec = []
    for i in range(len(robots_position)):
        res = robots_position[i] + velocities_arrays[i]
        temp = []
        if res[0] in range(len_x):
            temp.append(res[0])
        else:
            temp.append(res[0]%len_x)

        if res[1] in range(len_y):
            temp.append(res[1])
        else:
            temp.append(res[1]%len_y)

        first_sec.append(tuple(temp))


    return first_sec

def after_100_secs(robots_position, velocities_arrays, len_x, len_y):
    one_sec = after_1_sec(robots_position, velocities_arrays, len_x, len_y)
    # print('after 1 sec')
    for i in range(2, 101):
        # print(f'after {i} secs')
        one_sec = after_1_sec(one_sec, velocities_arrays, len_x, len_y)

    return one_sec

def visualize_robots_final(last_coords, basics):
    for i in range(len(last_coords)):
        if basics.iloc[(last_coords[i])] == '.':
            basics.iloc[(last_coords[i])]= 1
        else:
            basics.iloc[(last_coords[i])] += 1

    basics.iloc[:, int(len(basics.columns)/2)] = ' '
    basics.iloc[int(len(basics)/2), :] = ' '

    return basics

def return_four_sections(basics):
    cols = int(len(basics.columns)/2)
    rows = int(len(basics)/2)

    section_1 = 0
    for i in range(rows):
        for j in range(cols):
            if basics.iloc[i,j] != '.':
                section_1 += int(basics.iloc[i,j])

    section_2 = 0
    for i in range(rows):
        for j in range(cols+1, len(basics.columns)):
            if basics.iloc[i,j] != '.':
                section_2 += int(basics.iloc[i,j])

    section_3 = 0
    for i in range(rows+1, len(basics)):
        for j in range(cols):
            if basics.iloc[i,j] != '.':
                section_3 += int(basics.iloc[i,j])

    section_4 = 0
    for i in range(rows+1, len(basics)):
        for j in range(cols+1, len(basics.columns)):
            if basics.iloc[i,j] != '.':
                section_4 += int(basics.iloc[i,j])

    return section_1, section_2, section_3, section_4

def return_result(section_1, section_2, section_3, section_4):
    return section_1 * section_2 * section_3 * section_4
