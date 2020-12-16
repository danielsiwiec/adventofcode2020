import re

with open('input', 'r') as fd:
  lines = fd.read().split('\n')

memory = {}
mask = ''

def apply_mask(value, mask):
  return ''.join([v if m == 'X' else m for (v, m) in zip(value, mask)])

for line in lines:
  if 'mask' in line:
    mask = line.split(' = ')[1]
  else:
    match = re.search('\[(\d+)\] = (\d+)', line)
    address = int(match.group(1))
    value = int(match.group(2))
    binary = '{0:b}'.format(value).zfill(36)
    converted = apply_mask(binary, mask)
    memory[address] = int(converted, 2)

print(sum([v for k,v in memory.items()]))