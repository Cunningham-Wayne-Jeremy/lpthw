## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object created from the object Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## This will set the name of the name parameter to the instances value
        self.name = name

## Cat is-a object created from the object Animal
class Cat(Animal):

    def __init__(self, name):
        ##same
        self.name = name

## This is the base set or base object 
class Person(object):

    def __init__(self, name):
        ## This will set the name of the parameter to the instances value
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Creates an Employee class from person inheritting whatever person has
class Employee(Person):

    def __init__(self,name,salary):
        ## This is the same as self.name = name except for inherited instances
        super(Employee, self).__init__(name)
        ## 
        self.salary = salary
## 
class Fish(object):
    pass

## 
class Salmon(Fish):
    pass

## 
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ?? 
jesus = Cat("Jesus")

## 
mary = Person("Mary")

## 
mary.pet = jesus

## 
frank = Employee("Frank", 120000) 

## 
frank.pet = rover

## 
flipper = Fish()

##
crouse = Salmon()

## 
harry = Halibut()  
