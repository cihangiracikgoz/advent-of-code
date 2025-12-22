# Advent of Code - Day 4, Part 1

with open("day_04/input.txt", "r") as f:
    grid = []
    for line in f:
        line = line.rstrip("\n")
        if line:
            grid.append(line)

height = len(grid)
width = len(grid[0])

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1)]

valid = 0

for row in range(height):
    for column in range(width):
        if grid[row][column] == '.':
            continue

        forklift = "@" 
        neighbors = 0

        for drow, dcol in directions:
            nrow = row + drow
            ncol = column + dcol

            if nrow >= 0 and nrow < height and ncol >= 0 and ncol < width:
                if grid[nrow][ncol] == forklift:
                    neighbors += 1

        if neighbors < 4:
            valid += 1