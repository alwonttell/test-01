# number of company cars
cars = 100
# number of seats in each car
space_in_a_car = 4
# number of available drivers
drivers = 30
# number of passengers
passengers = 90
# number of cars not driven
cars_not_driven = cars - drivers
# number of driven cars
cars_driven = drivers
# carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# number of passengers per car
average_passengers_per_car = passengers / cars_driven


# returns number of company cars
print "There are", cars, "cars available."
# returns number of available drivers
print "There are only", drivers, "drivers available."
# returns number of cars not driven
print "There will be", cars_not_driven, "empty cars today."
# returns number of passengers we can transport
print "We can transport", carpool_capacity, "people today."
# returns number of passengers
print "We have", passengers, "to carpool today."
# returns number of passengers per car
print "We need to put about", average_passengers_per_car, "in each car."
# i change random things
