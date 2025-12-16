# Advent of Code - Day 2 - Part 2
import re

total = 0
invalid = re.compile(r'^(\d+)\1+$')

with open('day_02/input.txt') as f:
    for line in f:
        line = line.split(',')

        for i in line:
            start, end = i.split('-')

            for n in range(int(start), int(end) + 1):
                s = str(n)
                if invalid.match(s):
                    total += n