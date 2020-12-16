with open('input', 'r') as fd:
  lines = fd.read().split('\n')

def wait_time(bus, timestamp):
  mod = timestamp % bus
  return 0 if mod == 0 else bus - mod

timestamp = int(lines[0])
buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
wait_times = [wait_time(bus, timestamp) for bus in buses ]

print(min(wait_times) * buses[wait_times.index(min(wait_times))])

