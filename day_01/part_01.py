# Advent of Code - Day 1 Part 1

sp = 50
result = 0

with open('day_01/input.txt') as f:
    for line in f:
        line = line.strip()

        if line == '':
            continue

        direction = line[0]
        distance = int(line[1:])

        if direction == 'R':
            sp += distance
        elif direction == 'L':
            sp -= distance

        sp = sp % 100

        if sp == 0:
            result += 1

print("Result:", result)    

