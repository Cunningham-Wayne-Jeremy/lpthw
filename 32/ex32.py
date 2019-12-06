the_count = [1,2,3,4,5]
#print(the_count) That would actually print out the array INCLUDING the []'s so you will have to use
# a for loop to get all of the values out of this array
fruits = ['apples','oranges','pears','apricots']
#This is not a key value pair as it looks its actually a "mixed" array which is dumb but that means
#numbers and strings...

change = [1,'pennies', 2, 'dimes',3,'quaters']

#This first kind of for-loop goes through a list 
for number in the_count:
    print(f"This is count {number}")

#Most coding languages have you do loop unil i = array.length
#But for python you just say in array which is pretty cool!

#same as above 
#How is the below code know what fruit is? There is no variable called fruit...
#can this be literally be whatever you want it to be?
#YES that is correct! I didnt know this the whole time in for loops...
for whateveryouwanthere in fruits:   
    print(f"A fruit of type: {whateveryouwanthere}")

#also we can go through mixed lists too 
for i in change:
    print(f"I got {i}")

#We can also build lists, first start with an empty one
elements= []

#then use the range function (another built in function) to do 0 to 5 counts
#for i in range (0,6):
#    print(f"Adding {i} to the list.")
#    #append is a built in function that arrays use
#    elements.append(i)
#lets see if we can rewrite that code without a for loop

elements=list([0,1,2,3,4,5])
#YAY we did it!
for i in elements:
    print(f"Element was: {i}")

