#!/usr/bin/python3
from shared import read_from_file

expenses = list(map(lambda x: int(x), read_from_file('inputs/day1.txt')))

def getExpensesTwo(expenses):
  # return [x * y for x in expenses for y in expenses if x + y == 2020][0] # Not sure if pretty
  for x in expenses:
    for y in expenses:
      if x + y == 2020:
        return x * y

def getExpensesThree(expenses):
  for x in expenses:
    for y in expenses:
      for z in expenses:
        if x + y + z == 2020:
          return x * y * z

print("Part 1", getExpensesTwo(expenses))
print("Part 2", getExpensesThree(expenses))