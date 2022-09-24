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
now = time.gmtime()

def daily_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        cprint (('\n' + 'Qusstion >>> ' + str(question_num).center(70) + '>>> Of 6' + '\n'), 'red', attrs=['bold', 'underline'])
        cowsay.kitty(player_name + ', Test Your Knowledge!')
        cprint(('\n\n' + key.center(70) + '\n'), 'cyan', attrs=['bold'])
        
        print()
        for i in options[question_num-1]:
            cprint((i.center(70) + '\n\n'), 'yellow')
        guess = input(answer_options.center(70))
        print('\n')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        guess = guess.upper()
        question_num += 1
        getch.getch()
        os.system("clear")
    
    final_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        cprint((" CORRECT!".center(70) + '\n\n' + prs_any_key.center(70)), 'green', attrs=['bold'])
        return 1
    else:
        cprint(("NOT SO! Its ".center(70) + answer + "\n\n" + prs_any_key.center(70)), 'red', attrs=['bold'])
        return 0

def final_score(correct_guesses, guesses):
    os.system ('matrix -u21 3')
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
    cprint(("Your Grey Matter Score Today ".center(55) + str(score)+"%\n"), 'yellow')
    print(round_door.center(1) +'\n')
    
    if score <= 25:
        cprint(('Great Effort, There Is Room For Improvement!'.center(70)), 'red', attrs=["bold"])

    elif score <=  50:
        cprint(('Good Game, Keep It Up!'.center(70)), 'yellow', attrs=["bold"])

    else:
        cprint(('Outstanding, Great Score!'.center(70)), 'cyan', attrs=["bold"])
        
    # cprint('\n\n' + (prs_any_key.center(70) + '\n'), 'red', attrs=["bold", "blink"])

def try_again():

    replay = input('\nWOULD YOU LIKE TO REPLAY TODAY\'S GAME AGAIN? (Y or N) '.center(20))
    replay = replay.upper()

    # if replay == "YES":
    #     return True
    # else:
    #     return False
    # input()
    # replay = input

    # replay = input.upper()
    if replay == 'Y':
        return(True) 
    else:
        return(False) 

def count_down():
    now = time.localtime()
    count_down_hour = (24 - now[3]) 
    count_down_minute = (60 - now[4]) 
    print('Time Until New Game Questions >>> ', count_down_hour,'Hrs :', count_down_minute, 'Min')



questions = {
 "MUSIC: How Many Notes Are In Western Style Music? ": "A",
 "LORE: In The Lord Of The Rings, What Type Of Deity Is Melkor (Morgoth)? ": "S",
 """GEOGRAPHY: Which County Is This?\n   
                                                    ⢠⡤⡄⣾⣲⣦⣤⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣘⣿⣿⣷⣿⡿⠻⣿⣥⡄⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣤⣶⣿⣿⣿⣿⡏⠀⠀⠀⠏⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⢼⣿⣿⣿⠟⠙⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⣿⢿⣾⡿⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⣴⣿⠏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣾⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⢘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⢰⣾⣿⣿⣿⣿⣿⠿⠋⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠙⢿⣿⡿⠟⠁⠀ """ : "W",
 "ASTRONOMY: Earth Is The Only Planet Named After A Roman God? ": "Q",
 "CHEMISTRY: The chemical compound NaCl (sodium Chloride) is? ": "S",
 """GENERAL KNOWLEDGE: What Chess Piece Is This Called?\n 
                                |\_
                                /  .\_
                                |   ___)
                                |    }
                                |  =  |
                                /_____}
                               [_______] """ : "W"
}

options = [["Q. 9", "W. 22", "A. 12", "S. 16"],
          ["Q. Maiar", "W. Tyre", "A. Istari", "S. Valar"],
          ["Q. Finland", "W. Norway", "A. Cuba", "S. Japan"],
          ["Q. False", "A. True"],
          ["Q. Washing Powder", "W. Drain Cleaner", "A. Pool Chlorine", "S. Table Salt"],
          ["Q. Bishop", "W. Knight", "A. Pawn", "S. Rook"]]
         
print('\n')
cprint(colored(f.renderText(enter_name), 'red', attrs=['bold']))

print(epic_sword.center(1))

cprint(('\n' + player_name.center(70)), 'red', attrs=['bold'])
player_name = input()
# player_name = input('\n' + 'TYPE NAME TO LOAD: '.center(70))
player_name = player_name.upper()




os.system("clear")

daily_game()

# char = getch.getch()

while try_again():
    os.system("clear")
    daily_game()
   
os.system("clear")
cowsay.trex('Return For New\n Questions Tomorrow, \n' + player_name + '!')
print('\n')
count_down()
cprint(('\n' + time.asctime().center(100, '|') + '\n\n'), 'green', attrs=["bold", "reverse"])
    

    
#     new_game()


# while time.gmtime