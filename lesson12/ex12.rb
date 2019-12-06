print "Give me a number "
number = gets.chomp.to_i

bigger = number * 100
puts "A bigger number is #{bigger}"

print "Give me another number:"
another = gets.chomp
number = another.to_i

smaller = number / 100
puts "A smaller number is #{smaller} "

print "Give me one last number:"
tof = gets.chomp
puts "Lets see what to_f does #{tof}"

percent10 = tof.to_f * 0.10
chopitup = percent10.to_s.chop[0..4]
puts "Here is 10 percent of the last number #{chopitup}"
