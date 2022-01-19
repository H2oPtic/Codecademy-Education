import numpy as np

temperatures = np.genfromtxt('filename.csv', delimiter=',')

print(temperatures)

temperatures_fixed = temperatures + 3
monday_temperatures = temperatures_fixed[0,:]
thursday_friday_morning = temperatures_fixed[3:5, 1]

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]