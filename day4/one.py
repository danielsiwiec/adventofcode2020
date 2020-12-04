required_fileds = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]

def is_valid(passport):
  return all(field in passport for field in required_fileds)

with open("input", "r") as fd:
  passports = fd.read().split('\n\n')

valid = [passport for passport in passports if is_valid(passport)]
print(len(valid))