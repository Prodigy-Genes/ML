# finding the percentile for an array of numbers
# lets take an array of numbers and put them in a variable age

age = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# now to find the 75th percentile 
import numpy
_75percentile = numpy.percentile(age, 75)

print(f"The 75th percentile is : {round(_75percentile,2)}")

# finding the 90th percentile
_90percentile = numpy.percentile(age, 90)

print(f"The 90th Percentile is : {round(_90percentile, 2)}")