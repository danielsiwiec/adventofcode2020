import itertools

with open('input', 'r') as fd:
  steps = [int(line) for line in fd.read().split('\n')]

first = 0
steps.sort()
steps.insert(0, first)
last = steps[-1] + 3
steps.append(last)

deltas = [step - steps[index-1] for index, step in enumerate(steps[1:], start=1)]

optional_groups = []
current_ones_size = 0
for delta in deltas:
  if delta == 1:
    current_ones_size += 1
  else:
    if current_ones_size > 1:
      optional_groups.append(current_ones_size-1)
    current_ones_size = 0

options = 1
for one_group in optional_groups:
  options *= pow(2, one_group) - (one_group)//3 * ((one_group - 3) * 2 + 1 )

print(options)