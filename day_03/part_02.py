# Advent of Code - Day 3 - Part 2

total = 0
num = 12

with open("day_03/input.txt") as f:
    for line in f:
        line = line.strip()
        
        if line == '':
            continue

        stack = []
        remove = len(line) - num

        for i in line:
            while remove > 0 and stack and stack[-1] < i:
                stack.pop()
                remove -= 1
            stack.append(i)

        leftmost = stack[:num]
        jolt = int(''.join(leftmost))
        total += jolt

print("Total:", total)