directions = ['N', 'E', 'S', 'W']

class Ship:
  def __init__(self):
    self.facing = 'E'
    self.north = 0
    self.east = 0

  def turn(self, instruction):
    offset = int(instruction[1:]) // 90
    direction = instruction[0]
    facing_index = directions.index(self.facing)
    new_facing_index = (facing_index + offset) % 4 if direction == 'R' else (facing_index - offset) % 4
    self.facing = directions[new_facing_index]

  def move(self, instruction):
    direction = instruction[0]
    value = int(instruction[1:])

    if direction == 'N':
      self.north += value
    elif direction == 'S':
      self.north -= value
    elif direction == 'E':
      self.east += value
    elif direction == 'W':
      self.east -= value

  def forward(self, instruction):
    value = int(instruction[1:])
    if self.facing == 'N':
      self.north += value
    elif self.facing == 'S':
      self.north -= value
    elif self.facing == 'E':
      self.east += value
    elif self.facing == 'W':
      self.east -= value


  def instruction(self, instruction):
    action = instruction[0]
    if action in ['N', 'S', 'E', 'W']:
      self.move(instruction)
    elif action in ['R', 'L']:
      self.turn(instruction)
    elif action == 'F':
      self.forward(instruction)

  def manahatan(self):
    return abs(self.north) + abs(self.east)

with open('input', 'r') as fd:
  lines = fd.read().split('\n')

ship = Ship()

for instruction in lines:
  ship.instruction(instruction)
  # print(f'{instruction}, E:{ship.east}, N:{ship.north}, facing: {ship.facing}')

print(ship.manahatan())