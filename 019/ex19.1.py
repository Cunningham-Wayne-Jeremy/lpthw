# make a function with user input that will act as a calculator
def calculator(numberone, op, numbertwo):
    print(f"You have entered {numberone} {op} {numbertwo}")
    print(eval(f"{numberone} {op} {numbertwo}"))
# I didnt know back then but I could also do:
# return number1 operator number 2
# Not to say what I did was wrong!
calculator("90","/","2")

# Doesnt work, needs qoutes:
#calculator(100,-,6)

calculator('100-2',"--","300/5")

calculator("2^6","%","10")

calculator("(12/2)","**","100")

calculator("10000","-","9999")

calculator("3","/","5")

calculator("10","*","90")

calculator("400","+","-300")

calculator("5","<","10")
number1 = input("Enter the first number> ")
operator = input("Enter the operator> ")
number2 = input("Enter the second number>")

calculator(number1,operator,number2)
