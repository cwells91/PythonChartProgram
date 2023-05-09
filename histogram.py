import matplotlib.pyplot as plt

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115]

#ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140]

#plt.bar(ids, population_ages, label="Ages1")

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8, label='hist1')

plt.xlabel('Plot Number')
plt.ylabel('Important var')

plt.title('Interesting Graph')
plt.legend()

plt.show()