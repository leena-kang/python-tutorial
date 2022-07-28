# goal: translate lang where all vowels are not "g" (dog -> dgg)

def translate(phrase) : 
    translation = ""
    for letter in phrase: 
        # "in" funct -> checks if value has/includes following string 
        if  letter in "AEIOUaeiou":
            translation = translation + "g"
        else: 
            translation = translation + letter
    return translation 

# another way to control capitalizing 

def translate2(word):
    translation = "" 
    for letter in word: 
        if letter.lower() in "aeiou":
            if letter.isupper(): 
                translation = translation + "G"
            else: translation = translation + "g"
        else:
             translation = translation + letter 
    return translation 

print(translate2(input("Enter word: ")))