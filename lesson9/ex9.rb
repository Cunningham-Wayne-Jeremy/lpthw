#here is some more stuff I may not entirely understand
#Nah this is just an array
days = "Mon Tue Wed Thu Fri Sat Sun"
#I just understood SIMPLE coding tatic the escape character HAH
#I did it by reading the information in the book and putting it together
# it wasnt very clear but I realize now that the below array is a string
#thats obvious but to add a new line WITHIN a string you need to use an
#escape character to ESCAPE the string I just got that.
#That is why they are called escape characters DOUH!
months = "\nJan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAugust\nSeptember\nOctober\nNovember\nDecember"
#Prints the array days and months
puts "Here are the days: #{days}"
puts "Here are the months: #{months}"
#multi line paragraph with built in indention
puts %q{ There's something going on here.
  Its a qoute
  Kind of like a paragraph
  as many lines as we want
 }

#Testing my escape character theory
#This doesnt work:
#puts n n n n n n days
#I guess you still need the BACKSLASH
