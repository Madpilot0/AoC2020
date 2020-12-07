#!/usr/bin/python3
from shared import read_from_file

bags = read_from_file('inputs/day7.txt')

def parse_bags(bags):
  parsed_bags = {}
  for baglist in bags:
    blist = [baglist.split(" bags contain ")]
    for bag, contains in blist:
      if bag not in parsed_bags:
        parsed_bags[bag] = {}
      for contents in contains.replace(".","").replace(" bags","").replace(" bag", "").split(", "):
        if "no other" in contents: continue
        parsed_bags[bag][" ".join(contents.split(" ")[1:])] = int(contents.split(" ")[0])
  return parsed_bags

def traverse_gold(bags, bag, total=0):
  if not bags[bag]: return 0
  if "shiny gold" in bags[bag]: return 1
  mapped = map(lambda x: traverse_gold(bags, x, total), bags[bag])
  total += any(list(mapped))
  return total

def find_gold_bags(bags):
  num_bags = 0
  for bag in bags:
    num_bags += traverse_gold(bags, bag)
  return num_bags

def count_bags(bags, bag="shiny gold", total=0):
  if not bags[bag]: return 0
  for bag_in, amount in bags[bag].items():
    total += amount + amount * count_bags(bags, bag_in)
  return total

parsed_bags = parse_bags(bags)

print("Part 1:", find_gold_bags(parsed_bags))
print("Part 2:", count_bags(parsed_bags))