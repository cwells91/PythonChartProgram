#the purpose of this was to learn to draw charts using x and y data.
import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
plt.plot(x, y)

plt.xlabel('Plot Number')
plt.ylabel('Important var')

plt.title('Interesting Graph')

plt.show()