class Map:
    def __init__(self):
        with open("input", "r") as fd:
            self.map = [list(line) for line in fd.read().splitlines()]
            self.width = len(self.map[0])
            self.height = len(self.map)

    def get_tile_at_coordinates(self, row, col):
        return self.map[row][col % self.width]