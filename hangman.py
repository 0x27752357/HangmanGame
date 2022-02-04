import random 
from words import words
import string


def Random_Word(words) :
    word = random.choice(words) # choose random word from words.py using random 

    while "-" in word or " " in word : # some words got "-" and " " in it and well we don't want them 

        word = random.choice(words)

    return word # return the random word 


def HangMan() :
    Word = Random_Word(words)
    
    lives = 6 
     
    #print(Word) enable this to run some tests

    Word_Letters = set(Word)

    Alphabet = set(string.ascii_lowercase) 

    Used_Letters = set()


    while len(Word_Letters) > 0 and lives != 0 : 
        print(f"You have used this letters and you have {lives} lives left " , ' '.join(Used_Letters))

        Word_Tracker = [letter if letter in Used_Letters else '-' for letter in Word ]

        print("Current word is ",' '.join(Word_Tracker))  

        User_Letters = input("Guess the word : ").lower()
 
        if User_Letters in Alphabet - Used_Letters :
            Used_Letters.add(User_Letters)
            if User_Letters in Word_Letters :
               Word_Letters.remove(User_Letters)

            else :
                lives -= 1
                print("that was not right ! ")



        elif User_Letters in Used_Letters :
            print("You just guessed that letter ! ")
   
        else :
            print("Invalid letter !! ")
    
    if lives == 0 :
        print(f"You just killed a criminal \nwin win game btw \nand the word was {Word} ")
    else : 
        print("You saved the guy congrats !! ")







HangMan()

