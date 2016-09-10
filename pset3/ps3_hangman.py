# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "F:/notes/introduction/week 3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    
    for c in secretWord:
        if c in lettersGuessed:
            continue
        else  :
            return False     
    return True
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s=""
    for c in secretWord:
        if c in lettersGuessed:
            s=s+c
        else  :
            s=s+'_ '     
    return s



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s=""
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c in lettersGuessed:
            continue
        else :
            s=s+c
    return s        
                
    

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
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long'
    i=1
    s=''
    c=''
    guess=''
    lettersGuessed=[]
    while i<9:
        print '-----------'
        print 'You have '+str((9-i))+' guesses left'
        s=getAvailableLetters(lettersGuessed)
        print 'Available Letters: '+s
        guess=raw_input('Please guess a letter: ')
        guess=guess.lower()
        c = getGuessedWord(secretWord, lettersGuessed)   
        if guess in lettersGuessed:
            print 'Oops! You\'ve already guessed that letter: '+c
            continue
        lettersGuessed.append(guess) 
        c = getGuessedWord(secretWord, lettersGuessed)   
        if guess in secretWord :             
            print "Good guess: "+c
        else :
            print 'Oops! That letter is not in my word: '+c
            i+=1  
        res = isWordGuessed(secretWord, lettersGuessed)
        if  res:
            break
    print '-----------'
    if  res==True:
            print 'Congratulations, you won'       
    else  :
            print 'Sorry, you ran out of guesses. The word was '+ secretWord +'.'     
          
      
    
            
         





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
hangman('else')
