ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that!")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding" , next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")
    #Yea I know its a single qoute but it doesnt matter.
print('There we go: ', stuff)

print("Let's do some things with stuff.")

print(stuff[1]) #(Oranges)
print(stuff[-1]) #whoa! fancy!(Corn!)
print(stuff.pop())#Corn again?
print(' '.join(stuff))
something=" delimiter "
print(f'{something}'.join(stuff[2:5]))

