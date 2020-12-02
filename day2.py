#!/usr/bin/python3
from shared import read_from_file
import re

passwords = read_from_file('inputs/day2.txt')

def is_valid_password_count(passwords):
  valid_count = 0
  for password in passwords:
    first_num, second_num, character, pwd = list(filter(None,re.split('-|:|\\s', password)))
    first_num, second_num = [int(x) for x in [first_num, second_num]]
    if pwd.count(character) >= first_num and pwd.count(character) <= second_num:
      valid_count += 1
  return valid_count

def is_valid_password_char(passwords):
  valid_count = 0
  for password in passwords:
    first_num, second_num, character, pwd = list(filter(None,re.split('-|:|\\s', password)))
    first_num, second_num = [int(x) for x in [first_num, second_num]]
    if pwd[first_num - 1] == pwd[second_num  - 1]: 
      continue
    if pwd[first_num - 1] == character or pwd[second_num - 1] == character:
      valid_count += 1
  return valid_count

print("Part 1", is_valid_password_count(passwords))
print("Part 2", is_valid_password_char(passwords))