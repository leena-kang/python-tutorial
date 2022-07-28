phrase = "Giraffe Academy"

# " .function" to run a function 
#"is" indicates boolean (will output true/false)
print(phrase.upper().isupper()) 

 # len = function that outputs number of characters in that string
print(len(phrase))

# outputs the character corresponding to index num
print(phrase[0])

#returns index num of that character 
print(phrase.index("G"))
    #returns which index num it starts at 
print(phrase.index("Acad"))


#replace funt: (what to replace, replace with what)
print(phrase.replace("Giraffe", "Hippo"))