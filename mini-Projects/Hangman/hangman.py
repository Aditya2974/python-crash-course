# We have to pick a random word from a list : 
import random as rand
import string
from words import words

def get_valid_word(words):
    word = rand.choice(words)

    
    return word.upper()

def hangman():
    valid_word = get_valid_word(words);

    word_set = set(valid_word)

    alphabet = set(string.ascii_uppercase)

    guessed_letters = set() # keep track of already guessed letters.

    #get user input :
    while len(word_set) > 0: 

        print('You have already guessed '   , ' '.join(guessed_letters))

        # What the current word is :
        list_of_words = [letter if letter in guessed_letters else '-' for letter in valid_word]
        print('Current word : ', ' '.join(list_of_words))

        user_letter = input('Guess a letter : ').upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_set:
                word_set.remove(user_letter)
        
        elif user_letter in guessed_letters:
            print("Already used")
        else:
            print('Invalid character')

    
    print('Word was ', valid_word)
    print('Word guessed correctly!')


hangman()
