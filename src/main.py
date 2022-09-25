import time
import getch
from termcolor import colored, cprint
from pyfiglet import Figlet
from ascii import impossible_cube
import os

f = Figlet(font='colossal')
prs_any_key = (' >>> PRESS -- ANY -- KEY >>> ')
daily_title = ('DAILY')
game_title = ('GAME')


os.system('clear')
cprint((impossible_cube +'\n'), 'yellow')

cprint('\n\n' + (prs_any_key.center(70) + '\n'),
    'red', attrs=['bold', 'blink'])

cprint((daily_title.center(70) + '\n\n'),
    'cyan', attrs=['bold'])

cprint(colored(f.renderText(' G R E Y >>>\n MATTER'),
    'grey', attrs=['bold']))

cprint((game_title.center(70) + '\n\n'),
    'cyan', attrs=['bold'])

cprint((prs_any_key.center(70) + '\n\n'),
    'red', attrs=['bold', 'blink'])

cprint(('\n' + time.asctime().center(72, '|') + '\n\n'),
    'green', attrs=['bold', 'reverse'])

char = getch.getch()

os.system('clear')

import q_and_a