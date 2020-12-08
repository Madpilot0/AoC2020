#!/usr/bin/python3
from shared import read_from_file

program = read_from_file('inputs/day8.txt')

def run_program(program):
  cur_index = 0
  visited_indexes = set()
  accum = 0
  while True:
    if cur_index in visited_indexes:
      return accum
    
    visited_indexes.add(cur_index)
    operator, amount = program[cur_index].split(" ")
    
    if operator == "acc":
      accum = eval(f"{accum} {amount}")

    if operator == "jmp":
      cur_index = eval(f"{cur_index} {amount}")
    else:
      cur_index += 1

def fix_program(program, tested_nodes=set()):
  cur_index = 0
  visited_indexes = set()
  accum = 0
  has_changed = False
  while True:
    if cur_index == len(program):
      return accum
    if cur_index in visited_indexes:
      return fix_program(program, tested_nodes)
  
    visited_indexes.add(cur_index)
    operator, amount = program[cur_index].split(" ")

    if operator == "acc":
      accum = eval(f"{accum} {amount}")

    if cur_index not in tested_nodes and not has_changed:
      has_changed = True
      tested_nodes.add(cur_index)
      if operator == "jmp":
        operator = "nop"
      elif operator == "nop":
        operator = "jmp"
    
    if operator == "jmp":
      cur_index = eval(f"{cur_index} {amount}")
    else:
      cur_index += 1

print("Part 1:", run_program(program))
print("Part 2:", fix_program(program))