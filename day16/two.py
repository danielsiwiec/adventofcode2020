import re
import itertools

def parse_range(string):
  m = re.search('(\d*)-(\d*)', string)
  lower = int(m.group(1))
  upper = int(m.group(2))
  return lambda x: int(x) >= lower and int(x) <= upper

class Rule:
  def __init__(self, string):
    (self.name, rest) = string.split(': ')
    self.rules = [parse_range(string) for string in rest.split(' or ')]

  def passes(self, value):
    return any([rule(value) for rule in self.rules])

with open('input') as fd:
  lines = fd.read()

def parse_rules(rules_lines):
  return [Rule(line) for line in rules_lines]

(rules_text, rest) = lines.split('\n\nyour ticket:\n')
(my_ticket, other_tickets_text) = rest.split('\n\nnearby tickets:\n')
rules_lines = rules_text.split('\n')

other_tickets = other_tickets_text.split('\n')

rules = parse_rules(rules_lines)

def ticket_passes(ticket, rules):
  return all([True for field in ticket.split(',') if any([rule.passes(field) for rule in rules])])

passing_tickets = [ticket for ticket in other_tickets if ticket_passes(ticket, rules)]

def ticket_passes_rules_in_order(ticket, rules):
  return all(rule.passes(value) for (rule, value) in zip(rules, ticket.split(',')))

def valid_permutation(permutation, tickets):
  return all(ticket_passes_rules_in_order(ticket, permutation) for ticket in tickets)

right_permutation = next(permutation for permutation in itertools.permutations(rules) if valid_permutation(permutation, passing_tickets))

departure_rule_indices = [idx for (idx, rule) in enumerate(right_permutation) if 'departure' in rule.name]

my_ticket_fields = [my_ticket.split(',')[idx] for idx in departure_rule_indices]

print(my_ticket_fields)