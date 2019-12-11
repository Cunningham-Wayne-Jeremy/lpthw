import sys
script, input_encoding, error = sys.argv
# Without a conventional loop like while, this will loop until the line is null
# this is kind of amazing I didnt even notice this before but the function main keeps calling itself
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
#This will show the encoded string and the decoded string

def print_line(line, encoding, errors):
    next_lang = line.strip() # this simply strips the line break
    raw_bytes = next_lang.encode(encoding, errors=errors) # This encodes it to bytes in UTF-8
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

#Opens the language file and specifies what encoding to use
languages = open("languages.txt", encoding="utf-8")
#calling the function main and main calls another function and itself creating a loop
main(languages, input_encoding, error)
