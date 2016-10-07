# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open("D:/My Learning/MIT 6.00.1x/words.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    needed_letters = [] #list for letters that are need for word formation
    for letter in secretWord:
        if letter in lettersGuessed:
            needed_letters.append(letter)
    
    if len(needed_letters) == len(secretWord):
        return True
    return False             



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    match = [] #list for presentation of missing letters
    for letter in secretWord:
        if letter in lettersGuessed:
            match.append(letter)
        else:
            match.append("_")
    return "".join(match) #convert list into a string and return it               
            
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    result = [] #list for letters that has not been used yet
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        if letter not in lettersGuessed:
            result.append(letter)
    result = "".join(sorted(result))        
    return result        
         
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hagman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    flag = False
    lettersGuessed = [] #list for all letters that has been entered from player
    guesses = 8
    while not flag:
        print("-----------")
        print("You have " + str(guesses) + " guesses left")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        letter = str(input("Please guess a letter: "))
        
        if letter not in secretWord and letter not in lettersGuessed:
            lettersGuessed.append(letter)
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
            
            guesses -= 1
            
        elif letter in secretWord and letter in lettersGuessed or letter not in secretWord and letter in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
                      
        else:
            lettersGuessed.append(letter)
            print("Good guess: ", getGuessedWord(secretWord, lettersGuessed)) 
            
            
        if isWordGuessed(secretWord, lettersGuessed):
            print("-----------")
            print("Congratulations, you won!")
            flag = True
            
            
        if guesses == 0:
           
            print("-----------")
            print("Sorry, you ran out of guesses. The word was ", secretWord, ".")
            break         
            
            
        
        
                      
            
            
              






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
