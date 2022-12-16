import re
import numpy as np

with open("input") as file:
    data = [line.removesuffix("\n") for line in file]

# -802_154 < x < 3_980_003
#   35_725 < y < 4_282_497

sbl: list = []
# Test line
y = 2_000_000
# y=10

all_sbl: list = []
relevant_sbl: list = []

# Sensor at x=12, y=14: closest beacon is at x=10, y=16
for line in data:
    # => im Rechteck sind keine Becons, ausßer 1 an der Stelle bx, by
    sx, sy, bx, by = map(int, re.findall("[xy]=([0-9-]+)", line))

    mrad = abs(by - sy) + abs(bx - sx)
    sbl = (sx, sy, bx, by, mrad)

    all_sbl.append(sbl)
    if y in range(sy - mrad, sy + mrad):
        print(sbl)
        relevant_sbl.append(sbl)


# -802_144, 3_980_013
# size: 4_782_164
# for x in range(-1_802_144, 4_000_000):
    for y in range(0, 4_000_000 + 1):
        if y % 20_0000 == 0:
            print("%", end='')

        no_beacon_ranges: list = []
        for rsbl in all_sbl:
            sx, sy, bx, by, mrad = rsbl
            mrad -= abs(sy - y)
            if mrad > 0:
                no_beacon_ranges.append((sx - mrad, sx + mrad))

        for nbr in no_beacon_ranges:
            a, b = nbr
            for nbr2 in no_beacon_ranges:
                a2, b2 = nbr2
                if abs(a2 - a) == 1 or abs(b2 - b) == 1 or abs(a2 - b2) or abs(a - b):
                    print(f"Match at {y}!!\n")

# to low 4406724
#        5367037
#
