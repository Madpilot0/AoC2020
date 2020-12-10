#!/usr/bin/python3
from shared import read_from_file
from collections import Counter

joltages = list(map(lambda x: int(x), read_from_file('inputs/day10.txt')))

def joltage_difference(joltages):
  one_jump = 0
  three_jump = 1
  current_joltage = 0

  for jolt in sorted(joltages):
    if jolt - current_joltage == 1:
      one_jump += 1
    else:
      three_jump += 1
    current_joltage = jolt
  return one_jump * three_jump

def adapter_connection_counter(joltages):
  counter = Counter((0, ))
  for jolt in joltages:
    counter[jolt] += sum(counter[j] for j in range(jolt - 3, jolt))
  return counter[joltages[-1]]

joltages = sorted(joltages)
print("Part 1:", joltage_difference(joltages))
print("Part 2:", adapter_connection_counter(joltages))