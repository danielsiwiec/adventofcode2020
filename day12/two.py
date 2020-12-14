directions = ['N', 'E', 'S', 'W']

class Waypoint:
  def __init__(self):
    self.north = 1
    self.east = 10
  
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

  def turn(self, instruction):
    direction = 1 if instruction[0] == 'R' else -1
    offset = (direction * int(instruction[1:]) // 90) % 4

    if offset == 1:
      (self.east, self.north) = (self.north, -self.east)
    if offset == 2:
      (self.east, self.north) = (-self.east, -self.north)
    if offset == 3:
      (self.east, self.north) = (-self.north, self.east)
    

class Ship:
  def __init__(self):
    self.facing = 'E'
    self.north = 0
    self.east = 0
    self.waypoint = Waypoint()

  def forward(self, instruction):
    value = int(instruction[1:])
    self.north += value * self.waypoint.north
    self.east += value * self.waypoint.east

  def instruction(self, instruction):
    action = instruction[0]
    if action in ['N', 'S', 'E', 'W']:
      self.waypoint.move(instruction)
    elif action in ['R', 'L']:
      self.waypoint.turn(instruction)
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