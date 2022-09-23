import time
import getch
from termcolor import colored, cprint
from pyfiglet import Figlet
from ascii import impossible_cube
import os

# keyboard = controller()

f = Figlet(font='colossal')
prs_any_key = (" >>> PRESS -- ANY -- KEY >>> ")
title_the = ("THE")
title_game = ("GAME")
# os.system('cls')
# clock = time.asctime()

os.system("clear")
cprint((impossible_cube.center(20) +'\n'), 'yellow')

cprint('\n\n' + (prs_any_key.center(70) + '\n'), 'red', attrs=["bold", "blink"])

cprint((title_the.center(70) + '\n\n'), 'cyan', attrs=['bold'])

cprint(colored(f.renderText(' G R E Y >>>\n MATTER'), 'grey', attrs=['bold']))


cprint((title_game.center(70) + '\n\n'), 'cyan', attrs=['bold'])

cprint((prs_any_key.center(70) + '\n\n'), 'red', attrs=["bold", "blink"])
# cprint(colored(f.renderText(' >>>'), 'green', attrs=['bold']))
cprint(('\n' + time.asctime().center(72, '|') + '\n\n'), 'green', attrs=["bold", "reverse"])

char = getch.getch()

os.system("clear")
# os.system('cmatrix')

import qanda
qanda