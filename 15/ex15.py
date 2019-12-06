# imports the module argv
from sys import argv
# sets the arguments for this python script
script, filename = argv
# The open command opens the file and keeps it open waiting for other commands
txt = open(filename, "r")
# Prints a message usng the filename
print(f"Here's your file {filename}:")
# This will use the built in function read to read the contents of the file that
# Was opened previously
print(txt.read())
# This will prompt the user to enter the file name again
print("Type the filename again:")
# Accepts input from the user asking for the file name
file_again = input("> ")
# Opens the file name that was provided by the user
txt_again = open(file_again,"r")
# This will print the contents of the file using the read function with no
# parameters
print(txt_again.read())
# This will close the open file filename
txt.close()
# This will close the open file_again
txt_again.close()
