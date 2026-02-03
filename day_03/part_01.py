# Advent of Code - Day 3 - Part 1

total = 0

with open("day_03/input.txt") as f:
    for line in f:
        line = line.strip()
        
        if line == '':
            continue

        max_jolt = 0
        
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                jolt = int(line[i] + line[j])
                max_jolt = max(max_jolt, jolt)

        total += max_jolt  

print("Total:", total)