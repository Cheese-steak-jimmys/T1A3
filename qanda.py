from termcolor import colored, cprint
from pyfiglet import Figlet
from ascii import epic_sword, round_door
import cowsay
import time
import os
import getch

f = Figlet(font='kban', justify="center")
answer_options = ("Enter (Q, W, A, or S): ")
prs_any_key = (" >>> PRESS -- ANY -- KEY >>> ")
enter_name = ('ENTER NAME')
player_name = ('ENTER NAME TO CONTINUE')

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        cowsay.stegosaurus(player_name + ', Test Your Knowledge!')
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
    cprint(('\n' + ' G R E Y -- >>> -- MATTER '.center(70, ':')), 'green', attrs=['bold'])
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
    print("Your Grey Matter Score Today ".center(55) + str(score)+"%\n")
    print(round_door.center(1) +'\n')
    cprint('\n\n' + (prs_any_key.center(70) + '\n'), 'red', attrs=["bold", "blink"])
    
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
 "The chemical compound NaCl (sodium Chloride) is? ": "S",
 """What Chess Piece Is This Called?\n 
                                |\_
                                /  .\_
                                |   ___)
                                |    }
                                |  =  |
                                /_____}
                               [_______] """ : "W"
}

options = [["Q. 12", "W. 22", "A. 9", "S. 16"],
          ["Q. Mayar", "W. Tyre", "A. Illuvatar", "S. Valar"],
          ["Q. False", "A. True"],
          ["Q. Washing Powder", "W. Arsenic", "A. Adrenaline", "S. Table Salt"],
          ["Q. Bishop", "W. Knight", "A. Pawn", "S. Rook"]]
         
print('\n')
cprint(colored(f.renderText(enter_name), 'red', attrs=['bold']))

print(epic_sword.center(1))

cprint(('\n' + player_name.center(70)), 'red', attrs=['bold'])
player_name = input()
# player_name = input('\n' + 'TYPE NAME TO LOAD: '.center(70))
player_name = player_name.upper()



os.system('cmatrix -s') 
os.system("clear")

new_game()

char = getch.getch()

# while play_again():
#     new_game()

os.system("clear")
cowsay.trex('Return For New Questions Tomorrow, ' + player_name + '!')
print('\n')
cprint(('\n' + time.asctime().center(100, '|') + '\n\n'), 'green', attrs=["bold", "reverse"])
