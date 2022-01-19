print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 2

# Write an if statement below:

if planet == 1:
  print('Your weight on Venus is: ' +  str(weight * 0.91))
elif planet == 2:
  print('Your weight on Mars is: ' + str(weight * 0.38))
elif planet == 3:
  print('Your weight on Jupiter is: ' + str(weight * 2.34))
elif planet == 4:
  print('Your weight on Saturn is: ' + str(weight * 1.06))
elif planet == 5:
  print('Your weight on Uranus is: ' + str(weight * 0.92))
elif planet == 6:
  print('Your weight on Neptune is: ' + str(weight * 1.19))