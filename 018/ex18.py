# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# So how does Python know when the function begins and ends? It does so by
# the : and indentions
# without the indentions it would end the function
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
# are the variables or arguments local only? Lets try and print out arg1 to see
# if it keeps getting overwritten:
#print(f"What is the value of arg1? is it First!? {arg1}")
# Turns out it doesnt exist outside of the function which is why we can keep
# nameing the arguments the same
#SO can you name the a variable the same???
x=3
x=4
print(f"What is the value of x 3 or 4? The value is: {x}")
# Apparently the first time declares the variable but the second time x is
# overwritten, interesting.
