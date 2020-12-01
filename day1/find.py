with open('input', 'r') as fd:
  lines = fd.read().split('\n')

for num1 in lines:
  for num2 in lines:
    for num3 in lines:
      num1 = int(num1)
      num2 = int(num2)
      num3 = int(num3)
      if (num1+num2+num3 == 2020):
        print(num1*num2*num3)