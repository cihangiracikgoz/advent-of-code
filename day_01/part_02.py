# Advent of Code - Day 1 Part 2

sp = 50
result = 0

with open('day_01/input.txt') as f:
    for line in f:
        line = line.strip()

        if line == '':
            continue    

        direction = line[0]
        distance = int(line[1:])

        # Count full laps
        result += distance // 100

        # Update starting position and find the remainder
        remainder = distance % 100
        old_sp = sp

        # Update starting position and check for crossing zero
        if direction == 'R':
            sp = (sp + remainder) % 100
            if remainder > 0 and old_sp + remainder > 100 and old_sp != 0:
                result += 1
        elif direction == 'L':
            sp = (sp - remainder) % 100
            if remainder > 0 and old_sp - remainder < 0 and old_sp != 0:
                result += 1

        # When starting position is exactly 0
        if sp == 0:
            result += 1
    
    print(result)
