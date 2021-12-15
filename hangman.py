# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print(wordlist)
    print("  ", len(wordlist), "words loaded.")
    print(type(wordlist))
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word = choose_word(wordlist)
    


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guessed_word = ''.join(letters_guessed)
    return secret_word == guessed_word


def get_guessed_word(secret_word, letters_guessed, input_letter,guesses):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # print(secret_word)
    # print(letters_guessed)
    # print(input_letter)
    flag = False
    vowels = 'aeiou'
    alphabets = string.ascii_lowercase
    
    for i,letter in enumerate(secret_word):
        if letter == input_letter:
            letters_guessed[i] = input_letter
            flag = True
        
    
    if not flag:
        print(f"Oops! That letter is not in my word: {''.join(letters_guessed)}")
        guesses -= 1
    else:
        print(f"Good Guess: {''.join(letters_guessed)}")
        
    #print(letters_guessed)
    return letters_guessed,guesses
        
    #using recursion 
    #To Write the comparison of two strings using recursion 


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_alphabets = string.ascii_lowercase
    all_alphabets_list = list(all_alphabets)
    
    available_letters_list = []
    
    for letter in letters_guessed:
        all_alphabets_list.remove(letter)
    print(f"Available Letters: {''.join(all_alphabets_list)}")
    return ''.join(all_alphabets_list)
        
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    len_to_be_guessed = len(secret_word)
    letters_guessed = []
    guesses = 6
    warnings = 3
    available_letters = get_available_letters(letters_guessed)
    input_list = []
    
    
    for i in range(len_to_be_guessed):
        letters_guessed.append("_ ")
        
       
    print("Welcome to the game hangman!")
    print(f"I'm thinking of a word that is {len(secret_word)} letters long !")
    print("--------------------------------------------")
    print(f"you have {guesses} number of guesses left!")    
    print("Available letters to choose from are: ",available_letters)
    
    while guesses != 0:
        check = is_word_guessed(secret_word, letters_guessed)
        #print(check)
        if not check:
            print(f'You have {warnings} warnings')
            print(f'You have {guesses} guesses left')
            guessed_str = ''.join(letters_guessed)
            print(f'so far, you have guessed the following alphabets: {guessed_str}')
            available_letters = get_available_letters(input_list)
            guessed_word = input("Please guess a letter: ")
            if guessed_word in letters_guessed:
                print(f'You have already guessed this word.')
            elif guessed_word in input_list:
                print('Input not available! Retry!')
            else:
                if not guessed_word.isalpha() or len(guessed_word) > 1:
                    warnings -= 1
                    
                    if warnings < 1:
                        print(f'You have lost 1 guess. No. of available guesses: {guesses}')
                        guesses -= 1
                        warnings = 3
            
                    print(f"Warning! You can only input a lower case single alphabet. You have {warnings} warnings left after which",
                      "you will lose a guess")    
                else:
                    guessed_word = guessed_word.lower()
                    input_list.append(guessed_word)
                    letters_guessed,guesses = get_guessed_word(secret_word, letters_guessed, guessed_word,guesses)
                    
            if guesses == 0:
                print(f"You have lost the game. The secret word to be guessed was: {secret_word}")
        else: 
            print(f'Congragulations! You have won the game and guessed the correct word: {secret_word}')
            unique = set(''.join(letters_guessed))           
            print(f'Your total score for this game is: {guesses*len(unique)}')
            break
    
    
# secret_word = 'charlie' #the word to be guessed
# hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    
            other_word is passed as a string
            my_word is passed as a list
            
    '''
    
    listother_word = list(other_word)
    word_check = True if len(my_word) == len(listother_word) else False
  
    #print(f"Type of listother_word is: {type(listother_word)}")
    #print(f"Type of my_word: {type(my_word)})")
    if word_check == True: 
        for i,letter in enumerate(listother_word):
            if letter == my_word[i] or my_word[i] == "_ ":
                pass
            else:
                word_check = False
                break
    
    return word_check
    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
             
            
    Abdullah Azhar: my_word is passed as a list
    # '''
    possible_matches = []
    
    
    
    # This code splits the list of the words guessed so far into a string after removing the extra spaces 
    # for char in my_word:
    #     char = char.split()
    #     str_my_word += ''.join(char)
    
    # Iterating over each word in word list and comparing with the string of my words(str_my_word)
    
    
    for word in wordlist:
        check = match_with_gaps(my_word, word)
        if check == True:
            possible_matches.append(word)
    
    print(f'possible_matches: {possible_matches}')
        
            
        # if (len(word) == len(str_my_word)):
        #     word_added = ''
        #     for i in range(len(word)):
        #         if word(i) == str_my_word(i) or str_my_word(i) == "_":
        #             check = True
        #         else:
        #             check = False
                    
        #             break
    


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    len_to_be_guessed = len(secret_word)
    letters_guessed = []
    guesses = 6
    warnings = 3
    available_letters = get_available_letters(letters_guessed)
    input_list = []
    
    
    for i in range(len_to_be_guessed):
        letters_guessed.append("_ ")
        
       
    print("Welcome to the game hangman!")
    print(f"I'm thinking of a word that is {len(secret_word)} letters long !")
    print("--------------------------------------------")
    print(f"you have {guesses} number of guesses left!")    
    print("Available letters to choose from are: ",available_letters)
    available_letters = get_available_letters(input_list)
    while guesses != 0:
        check = is_word_guessed(secret_word, letters_guessed)
        #print(check)
        if not check:
            print(f'You have {warnings} warnings')
            print(f'You have {guesses} guesses left')
            guessed_str = ''.join(letters_guessed)
            print(f'so far, you have guessed the following alphabets: {guessed_str}')
            # available_letters = get_available_letters(input_list)
            guessed_word = input("Please guess a letter: ")
            if guessed_word in letters_guessed or  guessed_word in input_list:
                print(f'You have already guessed this word.')
            elif guessed_word == "*":
                show_possible_matches(letters_guessed)
            else:
                if not guessed_word.isalpha() or len(guessed_word) > 1:
                    warnings -= 1
                    
                    if warnings < 1:
                        print(f'You have lost 1 guess. No. of available guesses: {guesses}')
                        guesses -= 1
                        warnings = 3
            
                    print(f"Warning! You can only input a lower case single alphabet. You have {warnings} warnings left after which",
                      "you will lose a guess")    
                else:
                    guessed_word = guessed_word.lower()
                    input_list.append(guessed_word)
                    letters_guessed,guesses = get_guessed_word(secret_word, letters_guessed, guessed_word,guesses)
                    
            if guesses == 0:
                print(f"You have lost the game. The secret word to be guessed was: {secret_word}")
        else: 
            print(f'Congragulations! You have won the game and guessed the correct word: {secret_word}')
            unique = set(''.join(letters_guessed))           
            print(f'Your total score for this game is: {guesses*len(unique)}')
            break
        available_letters = get_available_letters(input_list)
    
# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

# ###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
