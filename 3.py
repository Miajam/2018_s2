# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
def change():
    global grid
    grid_ch = []
    for i in range(len(grid)-1, -1, -1):
        L_1 = []
        for j in range(len(grid)):
            L_1.append(grid[j][i])
        grid_ch.append(L_1)
    grid = grid_ch









def tri(a,b):
    if grid[a][b] == 0:
        return 0
    for size in range(2,len(grid)+1000000):
        for j in range(b-size+1, b+size):
            if not(0 <= a+size-1 < len(grid) and 0<=j<len(grid)) or grid[a+size-1][j] == 0:
                return size-1

def triangles_in_grid():
    add = {}
    for direction in 'NESW':
        add[direction] = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid)):
                size = tri(i,j)
                if size >= 2:
                    add[direction][size] += 1
        change()
    re_1 = []
    for direction in add:
        add[direction] = sorted(add[direction].items(),key = lambda x:x[0],reverse = True)
        if not add[direction]:
            re_1.append(direction)
    add = {k:add[k] for k in add if k not in re_1}
    return add

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
def generate_grid():
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] != 0:
                grid[i][j] = 1
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
