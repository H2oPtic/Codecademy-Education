train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
  celcius = (f_temp - 32) * 5/9
  return celcius

c_temp = f_to_c(100)
print(c_temp)

def c_to_f(c_temp):
  farenheit = c_temp * (9/5) +32
  return farenheit

f_temp = c_to_f(0)
print(f_temp)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print('The GE train supplies ' + str(train_force) +' Newtons of force.')

def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass) 
print(bomb_energy)
print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules')
