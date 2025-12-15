# Advent of Code - Day 1 Part 1

sp = 50
result = 0

with open('day_01/test.txt') as f:
    for line in f:
        line = line.strip()

        if line == '':
            continue

        direction = line[0]
        distance = int(line[1:])

        # Update starting position
        if direction == 'R':
            sp += distance
        elif direction == 'L':
            sp -= distance

        # Normalize starting position within 0-99
        sp = sp % 100

        # When starting position is exactly 0
        if sp == 0:
            result += 1

    print(result)
