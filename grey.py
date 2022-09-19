import time
from termcolor import colored, cprint
from pyfiglet import Figlet
import os

f = Figlet(font='colossal')
prs_any_key = (" >>> PRESS - ENTER - KEY >>> ")
title_the = ("THE")
title_game = ("GAME")
# os.system('cls')
# clock = time.asctime()
cprint(('\n' + time.asctime().center(72, '_') + '\n\n'), 'green', attrs=["bold", "reverse"])

cprint((prs_any_key.center(72) + '\n'), 'red', attrs=["bold", "blink"])

cprint((title_the.center(72) + '\n\n'), 'cyan', attrs=['bold'])

cprint(colored(f.renderText(' G R E Y >>>\n MATTER'), 'grey', attrs=['bold']))


cprint((title_game.center(72) + '\n\n'), 'cyan', attrs=['bold'])

cprint((prs_any_key.center(72) + '\n\n'), 'red', attrs=["bold", "blink"])
# cprint(colored(f.renderText(' >>>'), 'green', attrs=['bold']))

input()
# while input.getch:True
os.system("clear")
    

# while KeyboardInterrupt: True
import qanda
qanda