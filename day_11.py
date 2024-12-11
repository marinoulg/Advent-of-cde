import pandas as pd
import numpy as np
import time

def get_stones(path):
    data = open(path, 'r').read()
    stones = []
    for stone in data.split():
        stones.append(int(stone))
    return stones

def get_new_stones(stones):
    new_stones = []
    for stone in stones:
        # print('stone =', stone)
        if stone == 0:
            stone = 1
        elif len(str(stone))%2 == 0:
            split = int(len(str(stone))/2)
            stone = (int(str(stone)[:split]),int(str(stone)[split:]))
        else :
            stone *= 2024


        if isinstance(stone, tuple):
            new_stones.append(stone[0])
            new_stones.append(stone[1])
        else:
            new_stones.append(stone)
        # print(new_stones)

    return new_stones



if __name__ == '__main__':
    a = (time.time())
    print(time.ctime(a))
    print(a)
    path = 'data/day-11.txt'
    stones = get_stones(path)
    print(stones)
    print('iteration 0')
    new_stones = get_new_stones(stones)
    for i in range(1,75):
        print('\n✅ iteration', i)
        new_stones = get_new_stones(new_stones)
        # print(new_stones)

        print('length is', len(new_stones))
    # print(time.time())
        b = ((time.time()))
        # print(time.ctime(b))
        print('time taken until now is', b-a, 'seconds')
