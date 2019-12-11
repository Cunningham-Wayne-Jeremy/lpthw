def add(a,b):
    print("Entering the add function")
    print(f"ADDING {a} + {b}")
    return a + b
    print("Leaving the add function")
def subtract(a,b):
    print("Entering the subtract function")
    print(f"SUBTRACTING {a} - {b}")
    print("Leaving the subtract function")
    return a - b


def multiply(a,b):
    print("Entering the multiply function")
    print(f"MULTIPLYING {a} * {b}")
    return a * b
    print("Leaving the multiply function")

def divide(a,b):
    print("Entering the divide function")
    print(f"DIVIDING {a} / {b}")
    return a / b
    print("Leaving the divide function")

#calling the functions!

print("Let's do some math with just functons!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("here is a puzzle.")

what = add((add(age,subtract(height,weight))), subtract(height, multiply(weight,divide(iq,2))))

print("""I dont care what the value becomes but I think that the enter and leaving will look just like this:
        Entering the add function
        Entering the add function
        Entering the subtract function
        Leaving the subtract function
        Leaving the add function
        Entering the subtract function
        Entering the multiplcation function
        Entering the divide function
        Leaving the divide function
        Leaving the multiply function
        Leaving the subtract funtion
        Leaving the add function
        """)
print("That becomes: ", what, "Can you do it by hand?")

print("My answer is: " , what)
