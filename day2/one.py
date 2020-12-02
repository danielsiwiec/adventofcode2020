import re

with open('one_input', 'r') as fd:
  lines = fd.read().splitlines()

def check_line(line):
  split = line.split(':')
  
  policy = split[0].strip()
  password = split[1].strip()

  split = policy.split(' ')
  occurences = split[0]
  pattern = split[1]

  split = occurences.split('-')
  min_occurences = int(split[0])
  max_occurencecs = int(split[1])

  count = len(re.findall(pattern, password))
  return count <= max_occurencecs and count >= min_occurences

entry_validations = [ check_line(line) for line in lines ]
valid_entries = [ x for x in entry_validations if x == True ]

print(len(valid_entries))