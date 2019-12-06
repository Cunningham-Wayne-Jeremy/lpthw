print "How old are you? "
age = gets.chomp
 print "How tall are ye lad? "
 height = gets.chomp
 #Goes to a new line not because of the ''' but because of puts
 #QUestion everything you noticed but didnt research why DONT DO that
 #INVESTIGATE ALL THINGS dont damper your learning but not looking into it
 puts '''
 I still dont know the difference in puts and print
 but enter your weight
 '''
weight = gets.chomp
 print "Oh wait print cannot use escape sequences maybe? \n No it can.
 But can it call variables? Yes it can: #{age} well I havent a clue then\n"

 puts "So, you're #{age} old, #{height} tall and #{weight} heavy."

print "Other ways to use get? "
#there is interger, string,chop Lets try chop
puts "Seems like gets runs first huh?"
#Same line so print and leave a space after last word
print "Enter some text you want choped like a misspelled word "
misspelled = gets.chop[0..3]

puts misspelled
