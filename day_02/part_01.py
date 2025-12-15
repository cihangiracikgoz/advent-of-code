# Advent of Code - Day 2 - Part 1
ranges = []
total = 0

with open('day_02/input.txt') as f:
    for line in f:
        line = line.split(',')

        # Your code logic here
        for i in line:
            start, end = i.split('-')
            ranges.append((int(start), int(end)))

            for n in range(int(start), int(end) + 1):
                s = str(n)
                if len(s) % 2 != 0:
                    continue

                half = len(s) // 2
                if s[:half] == s[half:]:
                    total += n
                    
print(total)