import pprint
import time
import os

grid_size = (8, 8)
# empty_grid = [[0]*grid_size[0]]*grid_size[1]

glider = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

beacon = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

diehard = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

acorn = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]


def add_vector(width, height, v1, v2):
    return ((v1[0] + v2[0]) % width, (v1[1] + v2[1]) % height)

def get_cell(grid, pos):
    return grid[pos[1]][pos[0]]

def get_next_state(cell, neighborhood):
    num_alive_neighbors = sum(neighborhood)
    if num_alive_neighbors < 2:
        return 0
    if cell == 1 and num_alive_neighbors == 2:
        return 1
    if num_alive_neighbors == 3:
        return 1
    else:
        return 0

def get_neighborhood(grid, width, height, pos):
    return [
        get_cell(grid, add_vector(width, height, pos, (-1, -1))),
        get_cell(grid, add_vector(width, height, pos, (0, -1))),
        get_cell(grid, add_vector(width, height, pos, (1, -1))),
        get_cell(grid, add_vector(width, height, pos, (-1, 0))),
        get_cell(grid, add_vector(width, height, pos, (1, 0))),
        get_cell(grid, add_vector(width, height, pos, (-1, 1))),
        get_cell(grid, add_vector(width, height, pos, (0, 1))),
        get_cell(grid, add_vector(width, height, pos, (1, 1))),
    ]

def get_next_grid(grid):
    next_grid = []
    width = len(grid[0])
    height = len(grid)
    for j, y in enumerate(grid):
        next_grid.append([])
        for i, x in enumerate(y):
            next_grid[-1].append(get_next_state(x, get_neighborhood(grid, width, height, (i, j))))

    return next_grid

def play(initial):
    next_grid = initial
    while True:
        os.system("clear")
        pprint.pprint(next_grid)
        next_grid = get_next_grid(next_grid)
        time.sleep(0.1)

if __name__ == "__main__":
    play(glider)
