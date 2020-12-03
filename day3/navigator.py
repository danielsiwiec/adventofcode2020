class Navigator:
  def __init__(self, map, step_row, step_col):
    self.row = 0
    self.col = 0
    self.step_row = step_row
    self.step_col = step_col
    self.map = map
  
  def current_tile(self):
    return self.map.get_tile_at_coordinates(self.row, self.col)
  
  def move(self):
    self.row += self.step_row
    self.col += self.step_col

  def in_bounds(self):
    return self.row < self.map.height

  def traverse(self):
    trees_hit = 0

    while self.in_bounds():
      tile = self.current_tile()
      self.move()
      if tile == '#':
        trees_hit += 1
    
    return trees_hit