import random
import numpy as np
from matplotlib import pyplot as plt


def neighborAtState(ix, iy, grid, grid_size, state):
    a =  []
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = ix + i
            y = iy + j
            if x > -1 and x < grid_size and y > -1 and y < grid_size and grid[x][y] == state:
                a.extend([x, y])
    return a




p1 = 0.1
p2 = 0.1
p3 = 0.1
p4 = 0.1
p5 = 0.1


#### MAKE THE GRID ####
# Define the grid size
grid_size = 20

# Create a square grid of empty sites
grid = np.full((grid_size , grid_size), 0)

#plt.ion()

# Begin experiment
concentration = []
time = []
repetitions = 400
#total_grid_positions = grid_size * grid_size
for t in range(repetitions):
    oxygen = 0
    for ix,iy in np.ndindex(grid.shape):
        if grid[ix][iy] == 0:
            if np.random.normal() < p1:
                grid[ix][iy] = 1
        elif grid[ix][iy] == 1:
            oxygen = oxygen + 1
            if np.random.normal() < 0.5 and np.random.normal() < p2:
                grid[ix][iy] = 0
            elif np.random.normal() < p3:
                neighborsAtState0 = neighborAtState(ix, iy, grid, grid_size, 0)
                if len(neighborsAtState0) > 0:
                    r = random.randrange(len(neighborsAtState0) / 2)
                    grid[neighborsAtState0[r]][neighborsAtState0[r+1]] = 2
                    grid[ix][iy] = 2
        elif grid[ix][iy] == 2:
            oxygen = oxygen + 1
            if t > 100 and t < 200 and np.random.normal() < p4:
                grid[ix][iy] = 3
        elif grid[ix][iy] == 3:
            oxygen = oxygen + 1
            neighborsAtState2 = neighborAtState(ix, iy, grid, grid_size, 2)
            if len(neighborsAtState2) > 0 and np.random.normal() < p5:
                grid[ix][iy] = 0
    concentration.append(oxygen)
    time.append(t)

plt.xlabel('time')
plt.ylabel('oxygen')
plt.suptitle('Catalyst, p1=%0.1f, p2=%0.1f p3=%0.1f p4=%0.1f p5=%0.1f' % (p1, p2, p3, p4, p5))
plt.plot(time, concentration)
plt.show()
