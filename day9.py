#!/usr/bin/python3
from shared import read_from_file

xmas = list(map(lambda x: int(x), read_from_file('inputs/day9.txt')))
preamble = 25

def can_sum_to(numbers, sums_to):
  for x in numbers:
    for y in numbers:
      if x + y == sums_to:
        return True
  return False

def check_first_incorrect(numbers, preamble):
  for i in range(preamble,len(numbers) - 1):
    if not can_sum_to(numbers[i - preamble + 1: i + 1], numbers[i + 1]):
      return numbers[i + 1]
  return 0

def check_incorrect_set(numbers, target):
  numbers = [number for number in numbers if number < target]
  size = 2
  while size < len(numbers):
    for number in range(0, len(numbers) - size):
      if sum(numbers[number:number + size]) == target:
        return min(numbers[number:number + size]) + max(numbers[number:number + size])
    size += 1
  return 0

first_incorrect = check_first_incorrect(xmas, preamble)

print("Part 1:", first_incorrect)
print("Part 2:", check_incorrect_set(xmas, first_incorrect))