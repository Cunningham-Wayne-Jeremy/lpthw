#create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California ' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

# creates a basic set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}
# lets make this slightly more complicated and maybe add more cities to one dict? is that possible?
# add some more cities
# So when adding dictionaries you dont have to loop them like an array as they are associative.
# So what happens when you assign it again? is it overwritten? Errors out or what?
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
# Would you look at that! The * a string is acutally helpful!!!!
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print our some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state dict nested in the cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida  has: ", cities[states['Florida']])

# print every state abrreviation
print('-' * 10)
# huh you can do multiple i's in a for loop interesting!
# Also note that you can use list for dictionaries which is iteresting
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")

# Print every city in state   
print('-' * 10) 
for abbrev,city in list(cities.items()): 
    print(f"{abbrev} has the city {city}")

#now do both at the same time (not really at the same time as we arent calling the forloop for cities)
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#safely get a abbreviation by state that might not be there
print('-' * 10)
state = states.get('Texas')

# if not state is easier to write but its good to have alternatives
if state == True:
    print("YAY TEXAS!")
else: 
    print("Sorry no Texas")
    
#get a city with a default value to avoid errors
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
    
