def calculator(numberone, op, numbertwo):
    print(f"You have entered {numberone} {op} {numbertwo}")  
    sameline=print(end='')
    calc=numberone op numbertwo
    print(calc,sameline)
number1 = int(input("Enter the first number> "))
operator = input("Enter the operator> ")
number2 = int(input("Enter the second number>"))

calculator(number1,operator,number2)

