#!/usr/bin/python3
from shared import read_from_file

seatingmap = read_from_file('inputs/day11.txt')

def check_seats_neighbor(seatmap, row, column):
  neighbors = lambda x, y: [(x2, y2) for x2 in range(x - 1, x + 2)
                                     for y2 in range(y - 1, y + 2)
                                     if (-1 < x <= len(seatmap) and
                                         -1 < y <= len(seatmap[row]) and
                                         (x != x2 or y != y2) and
                                         (0 <= x2 < len(seatmap)) and
                                         (0 <= y2 < len(seatmap[row])))]
  return [seatmap[x][y] for x, y in neighbors(row, column)]

def count_full_seats_line(seatmap, row, column):
  count = 0
  check_directions = [[-1,-1], [0,-1], [1, -1], [-1, 0], [1,0], [-1, 1], [0,1], [1,1]]
  for direction in check_directions:
    distance = 0
    while True:
      distance += 1
      x = direction[0] * distance + column
      y = direction[1] * distance + row
      if not (y >= 0 and y < len(seatmap) and x >= 0 and x < len(seatmap[row])):
        break
      if seatmap[y][x] == "#":
        count += 1
        break
      if seatmap[y][x] == "L":
        break
  return count

def occupied(seatingmap):
  temp_map = []
  has_changed = False

  for row in range(0, len(seatingmap)):
    temp_row = ""
    for column in range(0, len(seatingmap[row])):
      if seatingmap[row][column] == "#" and check_seats_neighbor(seatingmap, row, column).count("#") >= 4:
        temp_row += "L"
        has_changed = True
      elif seatingmap[row][column] == "L" and check_seats_neighbor(seatingmap, row, column).count("#") == 0:
        temp_row += "#"
        has_changed = True
      else:
        temp_row += seatingmap[row][column]
    temp_map.append(temp_row)

  print("Map:")
  for l in temp_map: print(l)
  print("")

  if not has_changed:
    return sum(x.count('#') for x in temp_map)
  return occupied(temp_map)

def occupied2(seatingmap):
  temp_map = []
  has_changed = False
  
  for row in range(0, len(seatingmap)):
    temp_row = ""
    for column in range(0, len(seatingmap[row])):
      if seatingmap[row][column] == "#" and count_full_seats_line(seatingmap, row, column) >= 5:
        temp_row += "L"
        has_changed = True
      elif seatingmap[row][column] == "L" and count_full_seats_line(seatingmap, row, column) == 0:
        temp_row += "#"
        has_changed = True
      else:
        temp_row += seatingmap[row][column]
    temp_map.append(temp_row)

  print("Map:")
  for l in temp_map: print(l)
  print("")

  if not has_changed:
    return sum(x.count('#') for x in temp_map)
  return occupied2(temp_map)

print("Part 1:", occupied(seatingmap))
print("Part 2:", occupied2(seatingmap))