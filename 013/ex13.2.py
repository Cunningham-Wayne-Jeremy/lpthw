from sys import argv
ageinput = input("What is your age? ")
heightinput = input("What is your height? ")
weightinput = input("What is your wieght? ")

script, averageage, averageheight, averageweight = argv
#In the future we can add some conditional statements to compare the average to the user input and print other things below!!!
print(f"The average age is {averageage} but your age is {ageinput}.")
print(f"The average height is {averageheight} but your height is {heightinput}.")
print(f"The average weight is {averageweight} but your weight is {weightinput}.")
#ageinput = input()
#ageinput
