import numpy as np
import matplotlib.pyplot as plt


mu, sigma = 0, 1 
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 50, density=True) #bin s into 50 bins, normlised to probability density
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()

#for i in range(bins.size()):
print(bins.size)
