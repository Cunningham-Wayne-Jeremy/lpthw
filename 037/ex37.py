#So this excersise is about remembering and learning python symobols such as def and if and "and"
#To help me remember them I was tasked to write them all down in a python file that actually works
#So here we go:
from sys import exit
print("Here is a series of functions created by yours truly at any time feel free to cancel with control C")
print("Function 1")
def thisisafunction():
    headache=input("Does Jeremy have a headache? (True or False): ")
    
    if headache == "True":
        print("Jeremy has a headache")
    elif headache == "False":
        print("Jeremy took medicine and no longer has a headache so he will walk with you!")
    else:
        print("What the heck?")
thisisafunction()

print("Function number 2")
continueorno=input("Continue(y,n)? ")
if continueorno =="y":
    from sys import argv
    script,number1,number2,filename = argv
    import re
    def functiontwo(number1,number2):
        reg1 = re.findall("[0-9]",number1)
        reg2 = re.findall("[0-9]",number2)
        try:
            num1=float(number1)
            num2=int(number2)    
            print("The numbers entered added together are equal to: ", num1+num2)
        except ValueError:
            print("ERROR")
    functiontwo(number1,number2)
else:
    exit(0)

print("Function number 3")
continueorno=input("Continue(y,n)? ")
if continueorno =="y":
    def functionthree(filename):
        openit=open(filename)
        print(openit.read())
        
    functionthree(filename)
else:
    exit(0)

