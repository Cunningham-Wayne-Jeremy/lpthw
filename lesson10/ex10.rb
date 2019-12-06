#declares a variable that will tab at the front of some text
tabby_cat = "\tI'm tabbed in"
tabby_cat2 = "\t I'm tabbed in are we the same?"
#Nope there will be a space
#declares a variable that will have text split in the middle
persian_cat = "I'm split\non a line"
#declares a variable that will have a single \ before a and another after
backslash_cat = "I'm \\ a \\ cat."

#Creates a fat_cat variable that is a multilne qoute with """
#The variable will display a tabbed list with bullets
#The Grass item will be the same its just on the same line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

#Prints out the variables which have their own strings so it works
puts tabby_cat
puts tabby_cat2
puts persian_cat
puts backslash_cat
puts fat_cat

#DERP WONT SHOW UP as it goes through a carriage return
puts "DERP\rHELLO"
#DERP will show up This time
puts "DERP
\r
HELLO"

puts '''
What\'s the point of using this instead of """.
'''
puts "What does this look like no formatting"
puts "\aWhat does this look like with formatting"
puts "\bWhat does this look like with formatting"
#COOL you can specify cool symbols!!!! and you can paste them somewhere else!
#unicode value if you want hex use \h followed by the number of the symbol
puts "\u1211   What does this look like with formatting"
#Oh a new line lol
puts "\v\v\v\v\vWhat does this look like vertical tab"
#I dont know...
puts "\oooWhat does this look like with formatting"

#Alrighty so why use '''? Whats the difference?
puts '''
#
'''

puts """
#{tabby_cat}
"""

#The difference is ''' doesnt accept the use of #{}
#So according to the bonehead you would want to use ''' when you dont want your
#formatting to work just yet. My opinion? Dont use ''' at all its silly.
