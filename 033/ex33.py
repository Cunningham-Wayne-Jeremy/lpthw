def userinputwhileloop():

    i=1
    loopuntil= int(input("Enter an integer at which the loop will stop: "))
    numbers = []
    increment_value = 5#int(input("Enter a value the code increments by:"))
    for i in range(0,loopuntil,increment_value):
        print(f"At the top i is equal to {i}")
        numbers.append(i)
        print(f"What is the value of i? {i}")
        print("Numbers now: ", numbers)
        print("At the bottom i is {}".format(i))

        print("The numbers: ")

    for num in numbers:
        print(num)
userinputwhileloop()
