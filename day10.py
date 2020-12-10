#!/usr/bin/python3
from shared import read_from_file
#from collections import Counter

joltages = sorted(list(map(lambda x: int(x), read_from_file('inputs/day10.txt'))))

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
  #counter = Counter((0, ))
  adapter_counter = {0: 1}
  for jolt in joltages:
    adapter_counter[jolt] = 0
    for j in range(jolt - 3, jolt):
      if j == 0 or j in joltages:
        adapter_counter[jolt] += adapter_counter[j]
    # counter[jolt] += sum(counter[j] for j in range(jolt - 3, jolt))
  return adapter_counter[joltages[-1]]

print("Part 1:", joltage_difference(joltages))
print("Part 2:", adapter_connection_counter(joltages))