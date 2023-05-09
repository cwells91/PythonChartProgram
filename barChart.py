import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [5, 4, 6, 7, 3]

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x, y, label='Bars1', color='red')
plt.bar(x2, y2, label='Bars2', color='blue')

plt.xlabel('Plot Number')
plt.ylabel('Important var')

plt.title('Interesting Graph')
plt.legend()

plt.show()