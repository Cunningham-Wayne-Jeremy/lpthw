from sys import argv
# We are going to just import exists which is a funciton that will
# check to see if a file exists
from os.path import exists

# Sets the arguments for the script
script, from_file, to_file = argv

# Prints out what the script is actually doing
print(f"Copying from {from_file} to {to_file}")

# we could do these two in one line, how?

indata = open(from_file,"r").read()


# The len function will display the length of a file not in characters
# but in bytes
print(f"The input file is {len(indata)} bytes long")

# Exists will check to see if the file exists
# In the future we can make if statememnts based on this
print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit ENTER to continue, CTRL-C to abort." )
# input()

out_file = open(to_file,"w")
out_file.write(indata)

print("Alright, all done")

out_file.close();
# When combining open and read with one line you cannot or its not necessary to
# close it apparently
#indata.close();
