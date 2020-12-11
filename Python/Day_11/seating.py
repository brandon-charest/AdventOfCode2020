import numpy as np

LOC = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
grid = []
with open("./input.txt") as f:
    data = f.read().split("\n")
    for line in data:
        temp = []
        for ch in line:
            temp.append(ch)
        grid.append(temp)

rows = len(grid)
cols = len(grid[0])
changing = []


def check_directions(grid, i, j):
    taken = 0
    for x, y in LOC:
        new_x = i + x
        new_y = j + y
        if 0 <= new_x < rows:
            if 0 <= new_y < cols:
                if grid[new_x][new_y] == "#":
                    taken += 1
    return taken


def change_seats(grid, debug=False):
    done = False
    iteration = 0
    while not done:
        if debug:
            print(np.matrix(grid))
            print(f"iterations: {iteration}")
            iteration += 1
        changing = []
        for i in range(len(data)):
            for j in range(len(data[0])):
                char = grid[i][j]
                if char == ".":
                    continue

                elif char == "L":
                    if check_directions(grid, i, j) == 0:
                        changing.append([i, j, "#"])

                elif char == "#":
                    if check_directions(grid, i, j) >= 4:
                        changing.append([i, j, "L"])
                    else:
                        continue
        if not changing:
            done = True
        else:
            for x, y, c in changing:
                grid[x][y] = c


change_seats(grid)
# print(np.matrix(grid))
print(sum(x.count("#") for x in grid))
