import re
import numpy as np
from copy import deepcopy
import math

mat = []


def calc_routes(mat, routes):
    trees = []   
    for route in routes:
        temp = deepcopy(mat)
        trees.append(traverse(temp, route))
    return math.prod(trees)

def traverse(mat, routes=None):
    row, col, count = 0,0,0
    max_row, max_col = len(mat), len(mat[0])

    if not routes:
        RIGHT = 3
        DOWN = 1
    else:
        RIGHT = routes[0]
        DOWN = routes[1]

    while row < max_row - 1:       
        col += RIGHT
        row += DOWN   
        if col > max_col - 1:
            col -= max_col 
        char = mat[row][col]
        if char == '#':
            mat[row][col] = 'X'
            count += 1
        else:
            mat[row][col] = 'O' 
    return count


with open('./input.txt') as f:
     for line in f:
         line = line.replace('\n', '').replace(' ', '')
         mat.append([x for x in line])
routes = [[1,1], [3,1], [5,1], [7,1], [1,2]]


res = traverse(deepcopy(mat))
res1 = calc_routes(mat, routes)

print(res)
print(res1)

