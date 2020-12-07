#!/usr/bin/python3
from shared import read_from_file

boardingpasses = read_from_file('inputs/day5.txt')

def parse_passes(boardingpasses):
  boarding_ids = [1]
  for bpass in boardingpasses:
    row = int("".join(list(map(lambda x: "1" if x == "B" else "0", bpass[0:7]))), 2)
    column = int("".join(list(map(lambda x: "1" if x == "R" else "0", bpass[7:]))), 2)
    boarding_ids.append((row * 8) + column)
  return boarding_ids

def find_seat(boarding_ids):
  for seat in range(sorted(boarding_ids)[0], sorted(boarding_ids)[-1] +1):
    if seat not in boarding_ids and int(seat) > 10:
      return seat
  return 0

boarding_ids = parse_passes(boardingpasses)
print("Part 1:", max(boarding_ids))
print("Part 2:" , find_seat(boarding_ids))