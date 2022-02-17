import random
from words import words
import string


def viable_word(lst):
    '''Returns a random word from the list of words in the words.py file'''
    word= random.choice(lst)
    
    while '-' in word or ' ' in word:
        word= random.choice(lst)

    return word.upper()    


def hangman():
    word_to_guess=viable_word(words) 
    word_letters_to_guess= set(word_to_guess)
    alphabets= set(string.ascii_uppercase)
    
    user_letters= set() #letters that have been entered by the user
    lives=10
    

    
    while len(word_letters_to_guess)>0 and lives > 0:
        #print the words users have already used
        print(f'You have {lives} remaining. You have already entered these letters: ', ' '.join(user_letters))

        #current word and what it looks like
        word_list = [ letter if letter in user_letters else '_'  for letter in word_to_guess ]
       
        print('The current word is: ', ' '.join(word_list))

        user_letter= input('Guess a letter ').upper()

        if user_letter in alphabets-user_letters:
            user_letters.add(user_letter)
            if user_letter in word_letters_to_guess:
                word_letters_to_guess.remove(user_letter)

            else:
                lives=lives-1
                print('The letter you entered is not in the word.')

        elif user_letter in user_letters:
            print('You have already guessed this character')  

        else:
            print('You have entered a wrong character')  


    if lives==0:
        print('Sorry, you run out of lives and died')
    print(f'Good job. You guessed the {word_to_guess}. Niceeeeee ')


    #checks to see whether the user wants to play again
    choice = input('Do you want to play again? Y for yes and N for No'). upper()
    if choice== 'Y':
        hangman()
    else:
        print ('Goodbye for now') 
        quit


hangman()