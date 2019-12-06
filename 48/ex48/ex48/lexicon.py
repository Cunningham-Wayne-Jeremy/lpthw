def scan(raw):
    words = raw.split()
    directions = ("south", "north", "east", "west", "down", "up", "left", "right", "back")
    verbs = ("go","kill","eat","attack","stab","chop","smack","punch")
    stops = ("the","of","then","in","from","at","it")
    nouns = ("door","bear","princess","cabinet")
    numbers = str((list(range(0,99999))))
    errors = ("om")
    sentence = []
    for word in words:
        if word in directions:
            sentence.append(("direction", word))
        elif word in verbs:
            sentence.append(("verb", word))
        elif word in stops:
            sentence.append(("stop", word))
        elif word in nouns:
            sentence.append(("noun", word))
        elif word in numbers:
            sentence.append(("number", int(word)))
        else:
            sentence.append(("error", word))
    return sentence
#print(scan("99 100"))
# Code at a hight level
# I think we dont need to worry about the user input, we juse need to focus on the unit test.
# the end result of 48 and 49 is using the functions in 48 and combining it with the user input from 49 to turn user input into commands
# We will be splitting the words based on spacing with sentence.split. They we will be dividing up the words into categorys that are within the scanner
# function. These categories are direction words, verbs, stop words, nouns and numbers
# Remember we are not coding the entire solution just the part that splits the words, places them in a category and returns a tuple
