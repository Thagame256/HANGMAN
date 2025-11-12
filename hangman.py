

import random
import string

WORDLIST_FILENAME = "words.txt"



# Problem Set 2, hangman.py
# Name: HIGENYI ENOCK
# Collaborators: VS CODE CO-PILOT, VERCEL V0
# Time spent: One  week



# -----------------------------------
# HELPER CODE
# -----------------------------------


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

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
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

    
        
    
def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    
    # List comprehension to get the correctly guessed letters from "letters_guessed"
    # Creating a string of the correctly guessed letters from "letters_guessed" 
    win_list = [i for i in secret_word if i in letters_guessed]
    win_string = "".join(win_list)
    
    # Checking if the player has won by comparing * secret_word * == "win_str"
    return secret_word == win_string



def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # Creating a string of the correctly guessed letters from "letters_guessed"
    guessed = ""
    # Iterating over the seceret_word and letters guessed to get common letters
    for i in secret_word:
        if i in letters_guessed:
            guessed += i
        else:
            guessed += "*"
    # Returning the string guessed contaning correctly guessed letters in thier right position
    return guessed
    

def guesses_remaining(guess, guess_count, secret_word, letters_guessed):
    """guess_count = the number of guesses the user is remaining with. Starts at 10 guess
       secret_word = A string of lettes to be guessed by the user. Word to be guessed
       letters_guessed = a list of letters guessed by the user so far.

       Calculates the guesses remaining each time a guess basing on the user input and the game Rules
       wrong vowel = -2 guesses, wrong consonant = -1 guess, correct guess = no penalty
       already guessed letter = no penalty
       returns the updated guess_count
       """
    # Defining the vowels
    vowels = "aeiou"
  
    # Updating the guess_count basing on the guess and Penalty Rules/logic
    # Cases where the guess is in the secret_word. NO GUESS PENALTY
   
    if guess in secret_word:
         print(f'Good guess: {guess}')
    else:
        # When the guess is not in the secret_word. if it is a vowel: -2, else (its consonant): -1
         print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}' )
         if guess in vowels:
            # Cases when the user guess_count is < 2  and guesses an incorrect vowel. Ends the game in a LOSE
            if guess_count < 2:
              
               guess_count = 0
              
            guess_count -= 2
         # Handling consonants
         else:
             guess_count -= 1
    # Returning the guess_count so that its updated each time through the loop.
    return guess_count
 
            
def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # Creating a string of lowercase alphabetical letters
    lett_ers = string.ascii_lowercase
    # Create a list of letters that haven't been guessed yet
    available_letters = [letter for letter in lett_ers if letter not in letters_guessed]
    # Join the list back into a string containing letters not yet guessed
    final_str = "".join(available_letters)
    return final_str
         
def print_available_letters(letters_guessed):
    # For Print#ing the available letters only once to the user
    print_available_str = get_available_letters(letters_guessed)
    return (f'Available letters: {print_available_str}') 

    
def revealer(secret_word,letters_guessed):
    """As a starting point, we suggest writing a helper function that chooses a letter to reveal. It should take two arguments: the secret word and the string
of available letters (from get_available_letters). This helper function should create a string choose_from containing the unique letters that are in
both the secret word and the available letters.
"""
    # Checking to see the common letters between the secret_word and available letters
    
    letters_available = get_available_letters(letters_guessed)
    # Creating a list of letters that are in both the secret word and available letters
    choose_list = [letter for letter in secret_word if letter in letters_available]
    # Joining the list to form a string
    choose_from = "".join(choose_list)
    # Randomly selecting a letter from the string choose_from
    revealed_letter= random.choice(choose_from)
    # Revealing the letter to the user by adding it to the list of letters_guessed
    letters_guessed.append(revealed_letter)
    return revealed_letter
                             
  
             
def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
     
    #load_words()
    
    # Intializing game variables.
    guess_count = 10

    letters_guessed =[]

    # Welcoming th user to the game with a cute message.
    print(f"Welcome to Hangman!!")
    # Informing the user the length of the secret_word.
    print(f'I am thinking of a word that is {len(secret_word)} letters long')

    # THE MAIN GAME LOOP AND LOGIC.
   
    while guess_count > 0:
      
      # Print outs each guessing time through the loop.
    
      print(f"You have {guess_count} guesses left.")
      print(print_available_letters(letters_guessed))
      guess = str.lower(input("Please guess a letter:"))

      # Playing the game with the with_help feature
      if guess == "!" and with_help == True:
         # The guess_count must be >= 3 to use the revealer/help function
         if guess_count >= 3:
             revealed = revealer(secret_word,letters_guessed)
             print (f'letter revealed : {revealed}')
             print(get_word_progress(secret_word, letters_guessed))
             # Help penalty Costs 3 guesses. Updating guess_count after using the revealer
             guess_count -= 3
             continue # Skip validation and restart loop
         else:
            print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
            continue  # Skip validation and restart loop
            
      # Handling invalid input (numbers and symbols) "!" inclusive when with_help == False
      if len(guess) != 1 or not guess.isalpha(): 
         print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
         continue     # Restart loop incase of an invalid input
      
      # Handling already guessed letters
      if guess in letters_guessed:
         print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}  ")
         
         continue     # Restart the loop incase the guessed later has already been guessed
      
      # Counting and updating the guess_count each time through the loop.
      guess_count = guesses_remaining(guess, guess_count, secret_word, letters_guessed)

      # Adding the guess to the Already guessed letters.  
      letters_guessed.append(guess)
      #print(letters_guessed)

      #printing the word progress to the user.
      print(get_word_progress(secret_word, letters_guessed))

      
      # Checking to see if the user has guessed all the letters before the guess_count is 0
      if has_player_won(secret_word, letters_guessed):
         break         # Stop the loop if all letters in the secret_word have been guessed
      
    print("_" * 25)  
      
    # Printing the Congratulations message to a winning User
    if has_player_won(secret_word, letters_guessed) == True:
      uniq_letters = set(secret_word)
      total_score = ((guess_count + 4 * len(uniq_letters)) + (3 * (len(secret_word))))
      print(f'Congratulations, you won!')
      print(f'Your total score for this game is: {total_score}''')

      print("_" * 6) 

    # Printing the Losing message to a winning User    
    else: 
      guess_count == 0
      print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
      
      print("_" * 25) 


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True  # Change to True to test with_help functionality
     # (you'll want to be able to type "!" as a guess)
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.

    

