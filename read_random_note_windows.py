from random import randint
import os
cmd = "dir | findstr /R notes.txt$"
results = os.popen(cmd).read()
listed_results = results.split()
indexed_value = listed_results[3]
replace_comma = indexed_value.replace(",","")
total = int(replace_comma)
notes = open("notes.txt")
#motd = open("/etc/motd", "w")
count = 0
# I could do a get size of the file then do a range based on the bytes of that file then check for -'s and increase count by 1 then print out the line
# and continue printing the line until it encounters another --
# simplify the output of ls then use seek(bytes) to make the randint range to the amount of bytes! To make it scalable
notes.seek((randint(0,int(total))))

while count < 2:
    line = notes.readline()
    if '--' in line and count <= 2:
        count += 1
    elif '--' not in line and count > 0 and count <= 2:
        print(line, end="")
    else:
        continue

notes.close()
