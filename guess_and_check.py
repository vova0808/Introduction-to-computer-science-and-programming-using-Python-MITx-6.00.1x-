low = 0
high = 100
print("Please, think of a number between 0 and 100!")

guessing = True
while guessing:
    guess = int((low + high) / 2)
    print("Is your secret number ", guess, "?")
    user_input = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    if user_input == 'h':
        high = guess
        
    elif user_input == 'l':
        low = guess
    elif user_input == 'c':
        guessing = False
        print("Game over. Your secret number was " , guess)
    else:
        print("Sorry, I did not understand your input")
        
        







        
