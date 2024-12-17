import pandas as pd
import numpy as np

# FOR CROSSWORD
def get_data(path, length):
    data = open(path, 'r').read()
    data = data.split('\n')[:length]
    return data

def get_cw(data):
    cw = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            temp.append(data[i][j])
        cw.append(temp)
    cw = pd.DataFrame(cw)
    return cw

def find_robot(cw):
    for i in range(len(cw)):
        for j in range(len(cw.columns)):
            if cw.iloc[i, j] == '@':
                return (i,j)


# FOR CONSIGNES
def get_consignes(path, line):
    consignes = open('../data/example-day-15-1.txt', 'r').read()
    consignes = consignes.split('\n')[line]
    cons = []

    for i in range(len(consignes)):
        cons.append(consignes[i])

    return cons

def whats_behind(cw, coords, left=None, right=None, up=None, down=None):
    i,j = coords
    # cw.iloc[i,j]='@'

    if up:
        # what is cw.iloc[i-1, j] ?
        for k in range(1, i):
            if i-k < 1:
                return (i,j)
            elif cw.iloc[i-k, j] == 'O':
                next
                if cw.iloc[i-k-1, j] == '.':
                    return (i-1, j), (i-k-1, j)
            elif cw.iloc[i-k, j] == '.' \
                or '@': # useless bc there is only 1 robot but useful for tests
                return (i-k, j)
            else:
                return (i,j)
        return (i,j)

    if down:
        # what is cw.iloc[i+1, j] ?
        for k in range(i, len(cw)-1):
            pass
            # if i+k > max(range(len(cw)-1)):       # to modify
            #     print('s')
            #     return (i,j)
            # elif cw.iloc[i+k, j] == 'O':
            #     print('a')
            #     next
            #     if cw.iloc[i+k+1, j] == '.':
            #         print('b')
            #         return (i+1, j), (i+k+1, j)
            # elif cw.iloc[i+k, j] == '.':
            #     print('c')
            #     return (i+k, j)
            # else:
            #     print('m')
            #     return (i,j)
        print('d')
        return (i,j)



def go_up(sign, cw, coords):
    """
    This seems to be working...?
    """
    initial = coords

    a,b = whats_behind(cw, coords=coords, up=True)
    cw.iloc[initial] = '.'

    if sign == '^':
        if isinstance(a, tuple):
            cw.iloc[a] = '@'
            cw.iloc[b] = 'O'
            return a, cw
        else:
            cw.iloc[(a,b)] = '@'
            return (a,b), cw


def go_down(sign, cw, coords):
    pass





def go_left(sign, cw, new_coords):
    new_coords = tuple()

    if sign == '<':
        cw.iloc[new_coords] = '.'
        if cw.iloc[new_coords[0], new_coords[1]-1] == '#':
            new_coords = (new_coords[0], new_coords[1]-1)
        elif cw.iloc[new_coords[0], new_coords[1]-1] == '.':
            cw.iloc[new_coords[0], new_coords[1]] == '@'

        else:
            new_coords = new_coords

        cw.iloc[new_coords] = '@'

    new_coords = find_robot(cw)
    return new_coords, cw



def go_right(sign, cw, new_coords):
    if sign == '>':
        for k in range(new_coords[1]+1, len(cw.columns)-1):
            if cw.iloc[new_coords[0], k]=='.':
                cw.iloc[new_coords[0], k]= '@'
                break
            elif cw.iloc[new_coords[0], k]=='#':
                cw.iloc[new_coords]='@'
                break
            elif cw.iloc[new_coords[0], k]=='O':
                if len(cw)-1 != k:
                    cw.iloc[k-1, new_coords[1]]='@'
                    cw.iloc[new_coords[0], k]='O'
                    break

    # if sign == '>':
    #     cw.iloc[new_coords] = '.'
    #     if cw.iloc[new_coords[0], new_coords[1]+1] == '.':
    #         new_coords = (new_coords[0], new_coords[1]+1)
    #         cw.iloc[new_coords] = '@'
    #     elif cw.iloc[new_coords[0], new_coords[1]+1] == 'O':
    #         cw.iloc[(new_coords[0], new_coords[1]+1)]='@'
    #         cw.iloc[(new_coords[0], new_coords[1]+2)]='O'
    #     elif cw.iloc[new_coords[0], new_coords[1]+1] == 'O' \
    #         and cw.iloc[new_coords[0], new_coords[1]+2] == 'O':
    #         cw.iloc[(new_coords[0], new_coords[1]+1)]='@'
    #         cw.iloc[(new_coords[0], new_coords[1]+3)]='O'

            # for k in range(new_coords[0]+1, len(cw)-1):
            #     if cw.iloc[k, new_coords[1]] == '.':
            #         if len(cw) - 1 != k:
            #             cw.iloc[k, new_coords[1]] = 'O'
            #             break
            #         else:
            #             break
        # else:
        #     cw.iloc[new_coords] = '@'

    new_coords = find_robot(cw)
    return new_coords, cw


def go_up(sign, cw, new_coords):
#     if sign == '^':
#         cw.iloc[new_coords] = '.'
#         if cw.iloc[new_coords[0]-1, new_coords[1]] == '.':
#             cw.iloc[new_coords[0]-1, new_coords[1]] = "@"
#             new_coords = (new_coords[0]-1, new_coords[1])
#         else:
#             new_coords = new_coords

#         cw.iloc[new_coords] = '@'

#     new_coords = find_robot(cw)
#     return new_coords, cw
    pass


def go_down(sign, cw, new_coords):
    if sign == 'v':
        cw.iloc[new_coords] = '.'
        if cw.iloc[new_coords[0]+1, new_coords[1]] == '.':
            new_coords = (new_coords[0]+1, new_coords[1])
            cw.iloc[new_coords]='@'
        elif cw.iloc[new_coords[0]+1, new_coords[1]] == 'O':
            cw.iloc[(new_coords[0], new_coords[1])]='@'
            for k in range(new_coords[0]+1, len(cw)-1):
                if cw.iloc[k, new_coords[1]] == '.':
                    if len(cw.columns) - 1 != k:
                        cw.iloc[new_coords[0],k] = 'O'
                        break
                    else:
                        break
        else:
            cw.iloc[new_coords] = '@'

    new_coords = find_robot(cw)
    return new_coords, cw
