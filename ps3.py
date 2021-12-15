# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Abdullah Azhar 
# Collaborators : None
# Time spent    : 5 Hours 

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,'*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1 #freq.get(x,0) function is a 'safeway' to access a value in a dictionary for a key x.
                                    # if x is not present in the dictionary, this will NOT generate a KeyError but will return 
                                    # the value 0 (the second argument in the function get())
    return freq
	

# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    try:
        lower_word = word.lower()
        p1_score = 0
    
        for elem in lower_word:
            p1_score = p1_score + SCRABBLE_LETTER_VALUES[elem]
        
        
        p2_score = 7*len(lower_word) - 3*(n-len(lower_word)) if 7*len(lower_word) - 3*(n-len(lower_word)) > 1 else 1
        
        return p1_score*p2_score
    except:
        raise Exception('You have either entered a non str word or the length of the word')
   
    
    
    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n,VOWELS,CONSONANTS):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    #math.ceil()
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    num_vowels -= 1
    #print(f" num_vowels: {num_vowels}")

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        #print(f"random choice for vowels: {x}")
        hand[x] = hand.get(x, 0) + 1 #This command takes the existing value of x in the dictioary hand and adds 1 to it and sets the new value to the value of the key x
        #print(f"vowel: hand[x] is equal to {hand[x]}")
    hand['*'] = 1
    
    for i in range(num_vowels+1, n):    
        x = random.choice(CONSONANTS)
        #print(f"random choice for consonant: {x}")
        hand[x] = hand.get(x, 0) + 1
        #print(f"consonant: hand[x] is equal to {hand[x]}")
    
    #print(f"hand being dealt has the following keys: {hand.keys()}")
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    word = word.lower()
    
    for w in word:
        check = hand.get(w,0)
        if check >= 1 and new_hand.get(w,0) > 0:
            new_hand[w] = new_hand.get(w,0)-1
    #print('I was here to update the hand ')
    return new_hand
        
        
        
    

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    wildcard_index = word.find('*')
    word_copy = list(word)
    
    handcopy = hand.copy()
    #print(f"word input: {word}")
    
    if wildcard_index != -1:
        #print('I was here')
        for i,vowel in enumerate(VOWELS):
            word_copy[wildcard_index] = vowel
            word_replaced = ''.join(word_copy)
            #print(f"word_replaced : {word_replaced}")
            for w in word_replaced:
                check = handcopy.get(w,0)
                if check == 0 and i == len(VOWELS):
                    return False
                else:
                    i += 1
                    #handcopy[w] = handcopy[w] - 1
                flag = word_replaced in word_list
                if flag == True:
                    return True 
    else:
        for w in word:
            check = handcopy.get(w,0)
            if check == 0:
                return False
            else:
                handcopy[w] = handcopy[w]-1

        flag = word in word_list
        
        return flag 

            
    
        

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    length_hand = 0
    
    keys_hand = hand.keys()
    
    for key in keys_hand:
        length_hand = length_hand + hand[key]
    
    return length_hand
    
def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function

    #word_list = load_words()
    #n = int(input('Please enter the hand length: '))
    #hand = deal_hand(n)
    score = 0
    Quit_Flag = False
    
    while(calculate_handlen(hand)>0):
        print('Current Hand: ')
        display_hand(hand)
        user_entered_word = input("Enter word, or \"!!\" to indicate that you are finished:")
        if (user_entered_word == '!!'):
            Quit_Flag = True
            break
        else:
            check = is_valid_word(user_entered_word, hand, word_list)
            if check == True:
                score = score + get_word_score(user_entered_word, calculate_handlen(hand))
                print(f'Word match. Your score is: {score}')
            else:
                print('Invalid word entered')
        hand = update_hand(hand, user_entered_word)
            
    print(f'Ran out of letters')
    print(f'Total score for this hand: {score}')
    return score,Quit_Flag


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(n,hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    keys_hand = set(hand.keys()) #gives you the unique value of keys
    
    VOWELS_copy = set(VOWELS)
    CONSONANTS_copy = set(CONSONANTS)
    
    VOWELS_diff = VOWELS_copy.difference(keys_hand)
    CONSONANTS_diff = CONSONANTS_copy.difference(keys_hand)
    
    VOWELS_modified_str = ''.join(VOWELS_diff)
    CONSONANTS_modified_str = ''.join(CONSONANTS_diff)
    sub_hand = deal_hand(n, VOWELS_modified_str, CONSONANTS_modified_str)
    return sub_hand
    
    
    
    
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    Total_score = 0
    number_hands = int(input('Please enter the total number of hands: '))
    length_per_hand = int(input('Please enter the number of alphabets per hand: '))
    hands = []
    
    for i in range(number_hands):
        hand = deal_hand(length_per_hand,VOWELS,CONSONANTS)
        hands.append(hand)
        #print('Existing Hands: ')
        #display_hand(hand)
    
    repeat_hand_check = 'no'
    
    while (len(hands)>0):    
        
        if repeat_hand_check == 'no':
            current_hand = random.choice(hands)
        print(f" Current Hand: {current_hand}")
        
        sub_flag = input('Would you like to substitute a letter? (type either a "yes" or "no" only! : ')
        sub_flag = sub_flag.lower()
        
        
        if sub_flag == 'yes':
            letter_to_be_substituted = input('which letter would you like to replace: ')
            sub_hand = substitute_hand(length_per_hand,current_hand,letter_to_be_substituted)
            score,Quit_Flag = play_hand(sub_hand,word_list)
            Total_score += score
        elif sub_flag == 'no':
            score,Quit_Flag = play_hand(current_hand,word_list)
            Total_score += score
        else:
            print("Error! You can enter a \"yes\" or \"no\" only! ")
            
            
        if Quit_Flag == True:
            break
        else:
            Total_Score += score 
        
        repeat_hand_check = input("Would you like to replay the hand? : (type either a \"yes\" or \"no\" only! ")
        
        if repeat_hand_check == 'no':
            hands.remove(current_hand)
        
        
        
    if len(hands) == 0 or score == -1:
        print(f"Total score over all hands: {Total_score}")
        


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    

