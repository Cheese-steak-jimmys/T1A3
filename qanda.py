from termcolor import colored, cprint
from pyfiglet import Figlet
import cowsay
import os
import getch

f = Figlet(font='kban', justify="center")
answer_options = ("Enter (Q, W, A, or S): ")
prs_any_key = (" >>> PRESS -- ANY -- KEY >>> ")
enter_name = ('\n ENTER YOUR NAME \n')
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        cowsay.stegosaurus(player_name + ', Test Your Knowledge, Mortal!')
        cprint(('\n\n' + key.center(70) + '\n'), 'cyan', attrs=['bold'])
        
        print()
        # cprint((q), 'cyan', attrs=['bold'])
        for i in options[question_num-1]:
            cprint((i.center(70) + '\n\n'), 'yellow')
        guess = input(answer_options.center(70))
        print('\n')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        getch.getch()
        os.system("clear")
    
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        cprint((" CORRECT!".center(70) + '\n\n' + prs_any_key.center(70)), 'green', attrs=['bold'])
        return 1
    else:
        cprint(("NOT SO! Its ".center(70) + answer + "\n\n" + prs_any_key.center(70)), 'red', attrs=['bold'])
        return 0

def display_score(correct_guesses, guesses):
    cprint((' G R E Y -- >>> -- MATTER '.center(70, ':')), 'green', attrs=['bold'])
    print('\n')

    print("Answers: ".center(35), end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print('\n')

    print("Choices: ".center(35), end="")
    for i in guesses:
        print(i, end=" ")
    print('\n')

    score = int((correct_guesses/len(questions))*100)
    print("Your Grey Matter Score Today ".center(45) + str(score)+"%\n")
    cprint('\n\n' + (prs_any_key + '\n'), 'red', attrs=["bold", "blink"])
    
def play_again():

    response = getch.getch()
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
 "How Many Notes Are In Western Style Music? ": "Q",
 "In LOTR Lore, What Type Of Deity Is Melkor (Morgoth)? ": "S",
 "Earth Is The Only Planet That's Not Named After A Greek God? ": "A",
 "The chemical compound NaCl (sodium Chloride) is? ": "S"
}

options = [["Q. 12", "W. 22", "A. 9", "S. 16"],
          ["Q. Mayar", "W. Tyre", "A. Illuvatar", "S. Valar"],
          ["Q. False", "A. True"],
          ["Q. Wasing Powder", "W. Arsenic", "A. Adrenaline", "S. Table Salt"]]
         
cprint(colored(f.renderText(enter_name), 'red', attrs=['bold']))
player_name = input('TYPE NAME TO LOAD: '.center(70))
player_name = player_name.upper()

os.system('matrix 8') 
os.system("clear")

new_game()

char = getch.getch()

# while play_again():
#     new_game()

os.system("clear")
cowsay.trex('See You Tomorrow, ' + player_name + '!')
print('\n')
