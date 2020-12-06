def calculate_seat_id(str):
  row = calculate_row(str[:7])
  col = calculate_col(str[-3:])
  return row * 8 + col

def calculate_col(str):
  binary_list = ['0' if char == 'L' else '1' for char in str ]
  return int(''.join(binary_list), 2)

def calculate_row(str):
  binary_list = ['0' if char == 'F' else '1' for char in str ]
  return int(''.join(binary_list), 2)

with open("input", "r") as fd:
  seats = fd.read().split('\n')

seat_ids = [calculate_seat_id(seat) for seat in seats]
seat_ids.sort(reverse=True)
print(seat_ids[0])