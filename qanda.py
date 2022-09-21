from termcolor import colored, cprint
from pyfiglet import Figlet
import cowsay
import os
import getch

# f = Figlet(font='thick')
answer_options = ("Enter (Q, W, A, or S): ")
prs_any_key = (" >>> PRESS -- ANY -- KEY >>> ")

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        cowsay.cow('General Knowledge')
        cprint(('\n\n' + key.center(70) + '\n'), 'cyan', attrs=['bold'])
        
        print()
        # cprint((q), 'cyan', attrs=['bold'])
        for i in options[question_num-1]:
            print(i.center(70) + '\n\n')
        guess = input(answer_options.center(70))
        print('\n')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
        getch.getch()
        os.system("clear")
    
    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        cprint((" CORRECT!".center(70) + '\n\n' + prs_any_key.center(70)), 'green', attrs=['bold'])
        return 1
    else:
        cprint(("WRONG!\n\n >>> PRESS -- ANY -- KEY >>> "), 'red', attrs=['bold'])
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    # print("-------------------------")
    cprint(('\n\n' + "RESULTS".center(70, '.') + '\n\n'), 'green', attrs=['bold'])
    # print("-------------------------")

    print("Answers: ".center(35), end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print('\n')

    print("Choices: ".center(35), end="")
    for i in guesses:
        print(i, end=" ")
    print('\n')

    score = int((correct_guesses/len(questions))*100)
    print("Your score today is ".center(45)+str(score)+"%\n")
    cprint('\n\n' + (prs_any_key.center(70) + '\n'), 'red', attrs=["bold", "blink"])
    
# -------------------------
def play_again():

    response = getch.getch()
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python? ": "Q",
 "What year was Python created?: ": "W",
 "Python is tributed to which comedy group?: ": "A",
 "Is the Earth round?: ": "Q"
}

options = [["Q. Guido van Rossum", "W. Elon Musk", "A. Bill Gates", "S. Mark Zuckerburg"],
          ["Q. 1989", "W. 1991", "A. 2000", "S. 2016"],
          ["Q. Lonely Island", "W. Smosh", "A. Monty Python", "S. SNL"],
          ["Q. True","W. False", "A. sometimes", "S. What's Earth?"]]
TorF_questions = {
 "Who created Python? ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

TorF_options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
music_questions = {
 "Who created Python? ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

music_options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

geo_questions = {
 "Who created Python? ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

geo_options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

lore_questions = {
 "Who created Python? ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

lore_options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

os.system("clear")
cowsay.trex('See You Tomorrow!')
