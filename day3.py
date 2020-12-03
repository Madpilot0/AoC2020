#!/usr/bin/python3
from shared import read_from_file

tree_map = read_from_file('inputs/day3.txt')

def count_trees(tree_map, directions):
  x_pos = 0
  y_pos = 0
  move_right, move_down = directions
  tree_count = 0
  while y_pos < len(tree_map):
    if tree_map[y_pos][x_pos % len(tree_map[y_pos])] == "#":
      tree_count += 1
    y_pos += move_down
    x_pos += move_right
  return tree_count

count_multiple = [
  [1, 1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2]
]

res = 1
for count in count_multiple:
  res *= count_trees(tree_map, count)

print("Part 1", count_trees(tree_map, [3, 1]))
print("Part 2", res)