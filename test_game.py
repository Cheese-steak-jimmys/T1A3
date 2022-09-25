
#Testing Q and A function.
#expected return if input True      >>> NOT So! Its (answer)
#expected return if input False     >>> NOT So! Its (answer)

def test_daily_game():
    answer_options = ('Enter (Q, W, A, or S): ')
    user_answer = []
    correct_user_answer = 0
    quiz_question_number = 1
    for key in quiz_questions:
        print (('\n' + 'Question >>> ' + str(quiz_question_number).center(70)
            + '>>> Of 6' + '\n'), 'green',)
        
        print(('\n\n' + key.center(70) + '\n'), 'cyan')
        
        print()
        for i in options[quiz_question_number-1]:
            print((i.center(70) + '\n\n'), 'yellow')
        guess = input(answer_options.center(70))
        print('\n')
        guess = guess.upper()
        user_answer.append(guess)

        correct_user_answer +=  verify_answer(quiz_questions.get(key), guess)
        guess = guess.upper()
        quiz_question_number +=  1
        # getch.getch()
        # os.system('clear')
    
def verify_answer(answer, guess):

    if answer == guess:
        print(('CORRECT!'.center(70) + '\n\n'),
            'green')
        return 1
    else:
        print('NOT SO! Its '.center(70) + answer)
        return 0

# def final_score(correct_user_answer, user_answer):
#     os.system ('matrix -u21 3')
#     print(('\n' + ' G R E Y -- >>> -- MATTER '.center(70, ':')),
#      'green')
#     print('\n')

#     print('Answers: '.center(35),'')
#     for i in quiz_questions:
#         print(quiz_questions.get(i), ' ')
#     print('\n')

#     print('Choices: '.center(35), '')
#     for i in user_answer:
#         print(i, ' ')
#     print('\n')

#     score = int((correct_user_answer/len(quiz_questions))*100)
#     print(('Your Grey Matter Score Today '.center(55) + str(score)+'%\n'),
#         'yellow')
    
    
#     if score <=  25:
#         print(('Good Effort, There Is Room For Improvement!'.center(70)),
#             'yellow')

#     elif score <=   50:
#         print(('Great Game, Keep It Up!'.center(70)),
#             'blue')

#     else:
#         print(('Outstanding, Great Score!'.center(70)),
#             'cyan')
        
   

# def replay_quiz():

#     replay = input('\nWOULD YOU LIKE TO REPLAY TODAY\'S GAME? (Y or N) '.center(20))
#     replay = replay.upper()

#     if replay == 'Y':
#         return(True) 
#     else:
#         return(False) 

# def next_quiz_count_down():
#     now = time.localtime()
#     next_quiz_count_down_hour = (24 - now[3]) 
#     next_quiz_count_down_minute = (60 - now[4]) 
#     print('Time Until New Game quiz_Questions >>> ', 
#     next_quiz_count_down_hour,'Hrs :', next_quiz_count_down_minute, 'Min')


quiz_questions = {
 'MUSIC: How Many Notes Are In Western Style Music? ': 'A',
 'LORE: In The Lord Of The Rings, What Type Of Deity Is Melkor (Morgoth)? '
 : 'S',
 'ASTRONOMY: Earth Is The Only Planet Named After A Roman God? ': 'Q',
 'CHEMISTRY: The chemical compound NaCl (sodium Chloride) is? ': 'S',
#  """GENERAL KNOWLEDGE: What Chess Piece Is This Called?\n 
#                                  |\_
#                                 /  .\_
#                                 |   ___)
#                                 |    }
#                                 |  =  |
#                                 /_____}
#                                [_______] """ : 'W'
}

options = [['Q. 9', 'W. 22', 'A. 12', 'S. 16'],
          ['Q. Maiar', 'W. Tyre', 'A. Istari', 'S. Valar'],
        #   ['Q. Finland', 'W. Norway', 'A. Cuba', 'S. Japan'],
          ['Q. False', 'A. True'],
          ['Q. Washing Powder', 'W. Drain Cleaner', 'A. Pool Chlorine', 'S. Table Salt']]
