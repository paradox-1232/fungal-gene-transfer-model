
import numpy as np
import matplotlib.pyplot as plt

size = 20
grid = np.zeros((size, size))

# Start with one cell having gene
grid[size//2, size//2] = 1

steps = 50
prob_transfer = 0.2

def get_neighbors(x, y):
    neighbors = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < size and 0 <= ny < size:
            neighbors.append((nx, ny))
    return neighbors

gene_counts = []

for step in range(steps):
    new_grid = grid.copy()
    
    for i in range(size):
        for j in range(size):
            if grid[i, j] == 1:
                for nx, ny in get_neighbors(i, j):
                    if np.random.rand() < prob_transfer:
                        new_grid[nx, ny] = 1
    
    grid = new_grid
    gene_counts.append(np.sum(grid))

plt.plot(gene_counts)
plt.xlabel("Time")
plt.ylabel("Gene Count")
plt.title("Gene Spread Over Time")

plt.savefig("gene_spread.png")
plt.show()
