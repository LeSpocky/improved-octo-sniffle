# assign 100 to the variable 'cars'
cars = 100

# assign 4 to the variable 'space_in_a_car'
# (was float, but is just used to multiply something, int is sufficient)
space_in_a_car = 4

# assign the value 30 to the variable 'drivers'
drivers = 30

# assign 90 to 'passengers'
passengers = 90

# calculate the difference between cars and drivers and assign the
# result to the variable 'cars_not_driven'
cars_not_driven = cars - drivers

# copy the value from the variable 'drivers' and assign it to the
# variable 'cars_driven'
cars_driven = drivers

# multiply the contents of the variables 'cars_driven' and
# 'space_in_a_car' and assign the result to the variable
# 'carpool_capacity'
carpool_capacity = cars_driven * space_in_a_car

# calculate the number of avg passengers per car and assign it
average_passengers_per_car = passengers / cars_driven


# print the number of available cars, well print the contents of the
# variable 'cars' in between two arbitrary strings
print "There are", cars, "cars available."

# print another variable with some nice text around it
print "There are only", drivers, "drivers available."

# print another variable with some nice text around it
print "There will be", cars_not_driven, "empty cars today."

# print another variable with some nice text around it
print "We can transport", carpool_capacity, "people today."

# print another variable with some nice text around it
print "We have", passengers, "to carpool today."

# print another variable with some nice text around it
print "We need to put about", average_passengers_per_car, "in each car."
