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
  first_occurence = int(split[0]) - 1
  second_occurence = int(split[1]) - 1

  return (password[first_occurence] == pattern) != (password[second_occurence] == pattern)

entry_validations = [ check_line(line) for line in lines ]
valid_entries = [ x for x in entry_validations if x == True ]

print(len(valid_entries))