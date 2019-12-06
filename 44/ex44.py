# When you see PARENT functioname() or CHILD functionname() that just means that the following is a
# declared function of the PARENT or from the CHILD class
from textwrap import dedent
class Parent(object):

    def override(self):
        print("from PARENT override()")
        print(dedent("""
                    I want to know if self changes depending on the function that you print self from
                    My theory is that it will be the same but I will print self in each function to
                    make sure.This is the self from Parent.override():
                    \n""", self))
    def implicit(self):
        print("from PARENT implicit()")
        print("This is the self from Parent.implicit():\n ",self)
    def altered(self):
        print("from PARENT altered()")
        print("This is the self from Parent.altered(): \n", self)

class Child(Parent):

    def override(self):
        print("from CHILD overrid()")
        print("This is the self from Child.override(): \n", self)

    def altered(self):
        print("from CHILD, but BEFORE calling  PARENT altered() with super")
        super(Child, self).altered()
        print("from CHILD, but AFTER calling PARENT altered() with super")
        print("This is the self from Child.altered(): \n", self)

dad = Parent()
son = Child()

dad.altered()
print("\n")
son.altered()
