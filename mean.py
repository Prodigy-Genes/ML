# finding the mean of some values with python

# (32+111+138+28+59+77+97) / 7 = 77.4

import numpy

values = [32, 111, 138, 28, 59, 77, 97]
# finding the mean of the above is easily done as


# and then find the difference of each value from the mean
mean = numpy.mean(values)

squarelist =[]

# after finding the value for the mean we will need to subtract each value from the mean

for numbers in values :
    diff = round(mean, 1) - numbers
    print(f"\n{round(mean,1)} - {numbers} = {round(diff,1)}")
    
    # For each difference i get i must square it
    
    square = numpy.square(round(diff,1))
    print(f"\n{round(diff,1)}squared = {round(square,1)}")
    
    # The variance is the average number of these squared differences
    # now to find the variance
    squarelist.append(round(square,1))
    
variance = numpy.mean(squarelist)
print(f"\n\nThe Variance is {round(variance,2)}")
    
    
