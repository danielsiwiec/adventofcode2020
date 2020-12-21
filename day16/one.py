import re

def parse_range(string):
  m = re.search('(\d*)-(\d*)', string)
  lower = int(m.group(1))
  upper = int(m.group(2))
  return lambda x: int(x) >= lower and int(x) <= upper

class Field:
  def __init__(self, string):
    (self.name, rest) = string.split(': ')
    self.rules = [parse_range(string) for string in rest.split(' or ')]

  def passes(self, value):
    return any([rule(value) for rule in self.rules])

with open('input') as fd:
  lines = fd.read()

def parse_rules(rules_lines):
  return [Field(line) for line in rules_lines]

(rules_text, rest) = lines.split('\n\nyour ticket:\n')
(my_ticket, other_tickets_text) = rest.split('\n\nnearby tickets:\n')
rules_lines = rules_text.split('\n')

other_tickets = other_tickets_text.split('\n')

rules = parse_rules(rules_lines)

violations = []
for ticket in other_tickets:
  violations.append([int(field) for field in ticket.split(',') if all(not rule.passes(field) for rule in rules)])

print(sum([sum(violation) for violation in violations]))