def userinputwhileloop():

    i=1
    #Accepts user input and determines how long the loop will run for.
    loopuntil= int(input("Enter an integer at which the loop will stop: "))
    #declares an empty list
    numbers = []
    increment_value = int(input("Enter a value the code increments by:"))
    while i < loopuntil:
        print(f"At the top i is equal to {i}")
        numbers.append(i)
        #Here we add the value given by the user to i
        i += increment_value
        print("Numbers now: ", numbers)
        print("At the bottom i is {}".format(i))

    print("The numbers: ")

    for num in numbers:
        print(num)
#    return mynoargfunction()
# As I thought the above code is not needed as when the function is called the code executes all of 
# The print statments but its good to remember that you can make infinite loops    
userinputwhileloop()

