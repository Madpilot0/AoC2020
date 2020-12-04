#!/usr/bin/python3
from shared import read_from_file
import re

passport_inputs = read_from_file('inputs/day4.txt')

def process_passports(passports):
  all_passports = []
  p_i = {}
  for passport_input in passports:
    if passport_input == "":
      all_passports.append(p_i)
      p_i = {}
      continue

    items = passport_input.split(" ")
    for item in items:
      k, v = item.split(":")
      p_i[k] = v
  all_passports.append(p_i)
  return all_passports

def filter_invalids(passport):
  required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
  return True if all([field in passport for field in required_fields]) else False

def filter_byr(passport):
  return 1920 <= int(passport["byr"]) <= 2002

def filter_iyr(passport):
  return 2010 <= int(passport["iyr"]) <= 2020

def filter_eyr(passport):
  return 2020 <= int(passport["eyr"]) <= 2030

def filter_hgt(passport):
  if "cm" in passport["hgt"]:
    return 150 <= int(passport["hgt"].split("cm")[0]) <= 193
  if "in" in passport["hgt"]:
    return 59 <= int(passport["hgt"].split("in")[0]) <= 76
  return False

def filter_hcl(passport):
  return re.match(r"^#[0-9a-f]{6}", passport["hcl"])

def filter_ecl(passport):
  return passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]

def filter_pid(passport):
  return re.match(r"^[0-9]{9}$", passport["pid"])

def valid_passports(passports):
  return list(filter(filter_invalids, passports))

def valid_passports_by_values(passports):
  filters = [filter_byr, filter_iyr, filter_eyr, filter_hgt, filter_hcl, filter_ecl, filter_pid]
  for f in filters:
    passports = list(filter(f, passports))

  return passports

passports = process_passports(passport_inputs)

print("Total Passports:",len(passports))

valid_passport_list = valid_passports(passports)

print("Part 1", len(valid_passport_list))
print("Part 2", len(valid_passports_by_values(valid_passport_list)))
