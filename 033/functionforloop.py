def userinputwhileloop():

    i=1
    #Accepts user input and determines how long the loop will run for.
    loopuntil= int(input("Enter an integer at which the loop will stop: "))
    #declares an empty list
    numbers = []
    increment_value = int(input("Enter a value the code increments by:"))
    for i in range(0,loopuntil):
        print(f"At the top i is equal to {i}")
        #This line of code does nothing now. The i in the for loop is somehow different than the one
        #listed here below....
        i += increment_value
        numbers.append(i)
        print(f"What is the value of i? {i}")
        #Odd when rinning this code the first iteration it increases by the listed amount but after
        #it increments by one each time.
        print("Numbers now: ", numbers)
        print("At the bottom i is {}".format(i))

    print("The numbers: ")

    for num in numbers:
        print(num)
#    return mynoargfunction()
# As I thought the above code is not needed as when the function is called the code executes all of 
# The print statments but its good to remember that you can make infinite loops    
userinputwhileloop()

