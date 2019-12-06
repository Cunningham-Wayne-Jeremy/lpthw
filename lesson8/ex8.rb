#Interesting finally something interesting
# This will format strings somehow
# AHH I see its kind of like an object I think?
#Sort of I dont know if its an object but the below %{first}..%{second} ..etc are user paramaters
#So the formatter below is a variable that has 4 arguments
formatter = "%{first} %{second} %{third} %{fourth}"
#The below code will assign an integer value to all of the paramters in formatter.
 puts formatter % {first: 1, second:2, third:3, fourth:4}
 #The below code will assign a string value to all of the paramters in formatter.
 puts formatter % {first: "one", second: "two", third: "three", fourth: "four"}
 #The below code will assign a boolean value to all of the paramters in formatter.
 puts formatter % {first: true, second: false, third: true, fourth:false }
#The below code will assign itself to all of the paramters in formatter. So it will print each of the
#arguments 4 times
 puts formatter % {first:formatter, second: formatter,third: formatter,fourth: formatter}
# This will assign lnes of a shitty haiku to the formatter
 puts formatter % {
   first: "I had this thing",
   second: "That you could type up right",
   third: "But it didnt sing.",
   fourth: "So I said goodnight."
 }

 #alphanumeric means letters and numbers
