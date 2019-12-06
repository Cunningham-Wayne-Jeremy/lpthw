#Assigns a value to the variable car
cars = 100
# Sets the variable for how much space is in a car
space_in_a_car = 4.0
#Specifies how many drivers we have and assigns it to a variable
drivers = 30
#Specifies how many passengers there are and assigns it to a variable
passengers = 90
#Subtracts the cars from how many dirvers they have and assigns it to a variable
cars_not_drivern = cars - drivers
#Assigns the value of drivers to another variable called cars_driven
cars_driven = drivers
#Determins the carpool capacity maximum
carpool_capacity = cars_driven * space_in_a_car
#Determines the average number of passengers per car.
average_passengers_per_car = passengers / cars_driven

#Prints a string followed by the variable car
print("There are", cars , "cars avalable.")
print("There are only" , drivers, "drivers available.")
print("There will be", cars_not_drivern , "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car , "in each car.")
