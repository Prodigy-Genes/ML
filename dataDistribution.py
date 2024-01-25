# To visualize data we can use matplot lib to create a histogram
# To generate random data we can use numpy too

import numpy
import matplotlib.pyplot as plt

# To generate random uniform number 
random_numbers = numpy.random.uniform(0.0, 5.0, 10000) # this generates 250 random numbers between 0.0 to 0.5 uniformly

# and now to show this graphic we use
plt.hist(random_numbers, 10)
plt.show()