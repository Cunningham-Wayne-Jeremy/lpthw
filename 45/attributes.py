# In this excercise I will demonstrate how to return the attribute of a method. But first
# Let us return the attribute of a function

def myfunction():
    myarray = [1,2,3,4]
    return print(myarray)
# This fails becuase  myarray only exists within the function its not a global value....
# print(myfunction.myarray)
myfunction()

class myclass(object):
    myarray = [5,6,7,8]
    def myfunction(self, userinput):
        self.userinput = userinput
        myarray = [4,3,2,1]
        print(myarray)
        print(self.myarray)
        print(userinput)
a = myclass()

# that returns the class id and python describtion of the object
# print(a)

# this will print the array and a none...
print(a.myfunction("[8, 7, 6, 5]"))

# to this day I still dont know why this returns None....
