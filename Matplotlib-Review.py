from matplotlib import pyplot as plt

x = [5,10,15,20,25,30,35]
y1 = [53,8,64,21,85,94,37]
y2 = [84,68,214,45,84,38,34]

plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color ='gray', marker='o')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(['Cool', 'Not Cool'], loc=4)

plt.show()