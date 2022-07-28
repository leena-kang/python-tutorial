# building a guessing game

secret_word = "giraffe" 
guess = "" 
count = 0

while (guess != secret_word) and (count < 3):
    guess = input("Enter guess: ")
    count += 1

if count == 3:
    print("You lose!") 
else:
    print("You win!") 