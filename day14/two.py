import re

with open('input', 'r') as fd:
  lines = fd.read().split('\n')

memory = {}
mask = ''

def apply_mask(binary_address, mask):
  converted = ''.join([v if m == '0' else ('1' if m == '1' else 'X') for (v, m) in zip(binary_address, mask)])
  num_of_x = len([c for c in converted if c == 'X'])

  addresses = []

  for value in range(2**num_of_x + 1):
    copy = converted
    for replacement in '{0:b}'.format(value).zfill(num_of_x):
      copy = copy.replace('X', replacement, 1)
    addresses.append(copy)
  
  return addresses

for line in lines:
  if 'mask' in line:
    mask = line.split(' = ')[1]
  else:
    match = re.search('\[(\d+)\] = (\d+)', line)
    address = int(match.group(1))
    value = int(match.group(2))
    binary_address = '{0:b}'.format(address).zfill(36)
    addresses = apply_mask(binary_address, mask)
    for address in addresses:
      memory[address] = value

print(sum([v for k,v in memory.items()]))