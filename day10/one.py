with open('input', 'r') as fd:
  steps = [int(line) for line in fd.read().split('\n')]

steps.append(0)
steps.sort()
steps.append(steps[-1] + 3)

ones = 0
threes = 0
for index, step in enumerate(steps[:-1]):
  diff = steps[index+1] - step
  if diff == 1:
    ones += 1
  elif diff == 3:
    threes +=1

print(ones*threes)