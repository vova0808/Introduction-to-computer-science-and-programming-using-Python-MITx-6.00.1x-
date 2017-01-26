# In this problem, you'll create a program that guesses a secret number!
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive).
# The computer makes guesses, and you give it input - is its guess too high or too low?



print("Please think of a number between 0 and 100!")
low = 0
high = 100
found = False

while not found:
    guess = int((low + high) / 2)
    print("Is your secret number is " + str(guess) + "?")
    message = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if message == 'h':
        high = guess
    elif message == 'l':
        low = guess
    elif message == 'c':
        print("Game over. Your secret number was: ", guess)
        found = True
    else:
        print("Sorry, I did not understand your input.")
        
        
