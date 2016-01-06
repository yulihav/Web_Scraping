import requests 
import bs4
import sys

def game():
    print("Welcome to Capital Guess! ")
    while True:
        play_round()
        continue_playing = raw_input('\nDo you want to play again? [y, n] -->   ')
        if continue_playing == 'n':
            print("Thanks for playing! Cya l8r allig8r") 
            break
        else:
            print('-----------------------------------------------------------') 
            continue                           

def loading_caps():
    alpha1 = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    cap = ''
    response = requests.get("https://www.countries-ofthe-world.com/capitals-of-the-world.html")
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    capital = soup.findAll('table', attrs = {'class': 'tld cap'})
    return capital

def play_round():
    guess_counter = 0
    country = raw_input('\nPlease enter the country>   ')
    country = country.title()
    capital = loading_caps()
    for row in capital[0].findAll('tr'):
        for cell in row.findAll('td'):
            if cell.text == country:
                cap = cell.findNext().text
                cap = cap.strip()
    if cap == '':
        print("\nCountry does not exist.")
    else :
        while True:
            guess_counter += 1
            answer = raw_input('\nPlease enter your guess of the capital -->   ')
            answer = answer.title()
            if answer == 'No':
                print('%s' %cap)
                break
            if answer == cap:
                print('\nYou guessed right in %d guesses!!! Bravo!' %guess_counter)
                break
            else:
                print('\nTry again! Hint: it starts with the letter %s'\
                    '\nOr say "NO" if you want to see the answer)' %cap[0])


game()                
