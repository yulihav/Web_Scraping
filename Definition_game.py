try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup
import random

# Main game
def game():
    print('Welcome to WordGuess! ')
    while True:
        play_round()
        continue_playing = raw_input('\nDo you want to play one more round? [y, n] -->   ')
        if continue_playing == 'n':
            break
        else:
            print('-----------------------------------------------------------') 
            continue

def loading_words():
    #Load data from dictionary
    content = urlopen('https://www.randomlists.com/random-vocabulary-words')
    xml = content.read()
    content.close()
    soup = BeautifulSoup(xml, "lxml")
    #Create an array of  words
    wordspans = soup.findAll("span", { "class" : "support" })
    words = [span.string for span in wordspans]
    #Load tips
    tipspans = soup.findAll("span", { "class" : "subtle" })
    tips = [tip.string for tip in tipspans]
    #return list of tuples
    words_tips = dict(zip(words, tips))
    return words_tips

def play_round():
    word_tip_dict = loading_words()
    word_to_guess = random.choice(list(word_tip_dict.keys()))
    print('\n\nWhat does the word "{}" mean?'.format(word_to_guess))
    guess_counter = 0
    numerator = 0
    result_list = []
    #Create print with answer possibilities
    for word in word_tip_dict:
        numerator += 1
        result_list.append(word)
        print('{}. {}'.format(numerator, word_tip_dict[word]))
    #Guess loop
    while True:
        guess_counter += 1
        try:
            answer = int(raw_input('\nPlease enter the number of your answer? -->   '))
        except ValueError:
            print("\nThat's not an int! Try again -->   ")
            try:
                answer = int(raw_input('\nPlease enter the number of your answer? -->   '))
            except ValueError:
                print("\nThat's not an int! BYE")
                break
        if word_to_guess == result_list[answer-1]:
            print('\nYou guessed right in {} guesses!!! Bravo!'.format(guess_counter))
            break
        else:
            print('try again!')


game()            
