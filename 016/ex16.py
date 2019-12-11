from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that hit ENTER.")

input("?")

print("Opening the file...")
target = open(filename,"w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("Enter line 1: ")
line2 = input("Enter line 2: ")
line3 = input("Enter line 3: ")

print("I'm going to write these to the file.")

# target.write(line1,line2,line3)
# The above code fails .write takes ONE argument.

# Would this work: YES!

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Lets rewrite the above code with ONE target.write

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# You can also do it this way:
# target.write(f"{line1} \n {line2} \n {line3} \n")

print("And finally, we close it.")
target.close()
