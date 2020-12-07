import re
from functools import reduce

def extract_bags(str):
    m = re.match("(\w* \w*) bags contain", str)
    uber_bag = m.group(1)
    bags = [m.group(1) for m in re.finditer("\d+ (\w* \w*) bag", str) ]
    return {bag:[uber_bag] for bag in bags}

def merge_dicts(dict1, dict2):
  for bag, arr in dict2.items():
    if bag in dict1:
      dict1[bag] += arr
    else:
      dict1[bag] = arr
  
  return dict1

def bag_options(bags_dict, bag, set=set()):
  if bag in bags_dict:
    for a_bag in bags_dict[bag]:
      set = bag_options(bags_dict, a_bag, set | {a_bag})
    return set
  else:
    return set


with open("input", "r") as fd:
    lines = fd.read().split("\n")

bags_dicts = [extract_bags(line) for line in lines]
bags_dict = reduce(merge_dicts, bags_dicts)

options = bag_options(bags_dict, 'shiny gold')
print(len(options))
