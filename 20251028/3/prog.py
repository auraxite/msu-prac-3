class Maze:
    def __init__(self, dim=1):
        self.dim = dim
        grid_size = 2 * dim + 1
        self.grid = [["█"] * grid_size for _ in range(grid_size)]
        for r in range(dim):
            for c in range(dim):
                self.grid[2 * r + 1][2 * c + 1] = "·"

    def find_connected_cells(self, start_x, start_y, visited):
        discovered = set()
        temp_lab = Maze(self.dim)
        temp_lab.grid = [[v for v in r] for r in self.grid]
        if self.grid[start_y * 2 + 1][start_x * 2] == "·":
            if (start_x - 1, start_y) not in visited:
                visited.add((start_x - 1, start_y))
                discovered |= self.find_connected_cells(start_x - 1, start_y, visited)
        if self.grid[start_y * 2 + 1][(start_x + 1) * 2] == "·":
            if (start_x + 1, start_y) not in visited:
                visited.add((start_x + 1, start_y))
                discovered |= self.find_connected_cells(start_x + 1, start_y, visited)
        if self.grid[start_y * 2][start_x * 2 + 1] == "·":
            if (start_x, start_y - 1) not in visited:
                visited.add((start_x, start_y - 1))
                discovered |= self.find_connected_cells(start_x, start_y - 1, visited)
        if self.grid[(start_y + 1) * 2][start_x * 2 + 1] == "·":
            if (start_x, start_y + 1) not in visited:
                visited.add((start_x, start_y + 1))
                discovered |= self.find_connected_cells(start_x, start_y + 1, visited)
        return visited | discovered

    def __setitem__(self, index_tuple, value):
        x_first = index_tuple[0]
        y_first = index_tuple[1].start
        x_second = index_tuple[1].stop
        y_second = index_tuple[2]
        x_min, x_max = min(x_first, x_second), max(x_first, x_second)
        y_min, y_max = min(y_first, y_second), max(y_first, y_second)
        if y_min == y_max:
            for pos in range(2 * (x_min + 1), 2 * x_max + 1, 2):
                self.grid[2 * y_min + 1][pos] = value
        if x_min == x_max:
            for pos in range(2 * (y_min + 1), 2 * y_max + 1, 2):
                self.grid[pos][2 * x_min + 1] = value
        return value
    
    def __getitem__(self, index_tuple):
        x_start = index_tuple[0]
        y_start = index_tuple[1].start
        x_end = index_tuple[1].stop
        y_end = index_tuple[2]
        connected_cells = self.find_connected_cells(x_start, y_start, set())
        return (x_end, y_end) in connected_cells

    def __str__(self):
        return "\n".join("".join(r) for r in self.grid)

import sys
exec(sys.stdin.read())

'''
m = Maze(4)
print(m)
print(m[0,0 : 1,0], m[0,0 : 2,2], m[1,0 : 1,2])
m[0,0 : 0,3] = m[0,3 : 3,3] = m[3,3 : 3,0] = m[3,0 : 2,0] = m[2,0 : 2,2] = m[1,0 : 1,2] = "·"
print(m)
print(m[0,0 : 1,0], m[0,0 : 2,2], m[1,0 : 1,2])
'''