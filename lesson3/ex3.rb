#here are the mathematical operators associated with Ruby
#+ add
#- subtrat
#/ divide
#* multiply
#% SO appararently this will check for remainders
#So this is how % works it divides by the specified number then it will
#display the rest that wasnt divisible or in other words 25 % 6 will
#take 25 and six goes into it 4 times OR 6 * 4 is 24 and 25 -24 is 1
#So that is what is left. The 1 Its the same as division in math
# the remaineder
#< less than obv
#> greater than obv
#<= obv
#>= obv
# I was so wrong on PEMDAS or the mathematical order of things
# I thought it was in order but ITS NOT its actually: PE(M&D)(A&S) .
#SO parenthesis, Exponents , multiplicateion and DIVISION at the same
#time then ADD and subtract at the same time lol didnt know this and
#I am 31
puts "I will now follow a stupid excercise counting retarded chickens:"

puts "Hens #{25.0 + 30 / 6}"
puts "Roosters #{100 - 25 * 3.0 % 4}"

puts "Now I will count the eggs:"

puts 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6.0

puts 3 + 2 < 5 - 7

puts "What is 3 +2? #{3.0 + 2}"
puts "what is 5 - 7? #{5 - 7.0}"

puts "Oh, that is why its false"

puts "Is it greater? #{5 > -2.0}"
puts"Is it greater or equal? #{5.0 >= -2}"
puts "Is it less or equal? #{5 <= -2.0}"

puts 25 % 6
