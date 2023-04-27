import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115]

ids = [x for x in range(len(population_ages))]

plt.bar(ids, population_ages, label="Ages1")

plt.xlabel('Plot Number')
plt.ylabel('Important var')

plt.title('Interesting Graph')
plt.legend()

plt.show()