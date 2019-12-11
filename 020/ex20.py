from sys import argv

script, input_file = argv

# bad choice of parameter f is for formatting usually but in this case its for
# file. This will read the files contents
def print_all(f):
    print(f.read())
# This will rewind the file to 0 which is necessary otherwise we would be at the
# end of the file for the print line by line command ahead
def rewind(f):
    f.seek(0)
# How does it know to print only 1 line? AHH there it is readline is controlling
# and specifying what line to read. When you run it again the next line is read.
# current_line does nothing other than print the line number increasing it each
# time manually keeps it accurate.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# It makes sense to declare this outside of the functions so that each one can
# use this variable. It takes the supplied file given at the terminal and opens
# it in default mode.
current_file = open(input_file)

# Actually calling the functions
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")
#This starts at line 1 as we previously used f.seek(0) so there is no magic 
#As to how to get it to print out at a specific line. 
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
