single_digits = range(10)
squares = []

for num in single_digits:
  squares.append(num**2)
  print(num)

print(squares)

cubes = [sin ** 3 for sin in single_digits]
print(cubes)