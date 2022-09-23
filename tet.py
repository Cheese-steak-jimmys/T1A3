import time

# yourCommand = "timeout 2s "
# timeoutSeconds = 2
# subprocess.call('cmatrix timeout 2s', shell=True)
# subprocess.call('matrix -s timeout 2s', shell=True,)
def count_down():
    now = time.localtime()
    count_down_hour = (24 - now[3]) 
    count_down_minute = (60 - now[4]) 
    print (count_down_hour,':', count_down_minute)

count_down()

# def next_play():

#     if (now[3]) <= 23:
#         return(True) 
#     else:
#         return(False) 



# while next_play():
#     print('grgggg')
#     break
# # new_game()
     
# else: print ("""

#                .....
#            .;;;;;;;;;,
#           ;;;'    `;;;,
#          ;;;'      `;;;
#          ;;;        ;;;
#          ;;;.      ;;;'
#          `;;;.    ;;;'
#           `;;;.  ;;;'
#            `;;',;;'
#             ,;;;'
#          ,;;;',;' ...,,,,...
#       ,;;;'    ,;;;;;;;;;;;;;;,
#    ,;;;'     ,;;;;;;;;;;;;;;;;;;,
#   ;;;;'     ;;;',,,   `';;;;;;;;;;
#  ;;;;,      ;;   ;;;     ';;;;;;;;;
# ;;;;;;       '    ;;;      ';;;;;;;
# ;;;;;;            .;;;      ;;;;;;;
# ;;;;;;,            ;;;;     ;;;;;;'
#  ;;;;;;,            ;;;;   .;;;;;'
#   `;;;;;;,           ;;;; ,;;;;;'
#    `;;;;;;;,,,,,,,,,, ;;;; ;;;'
#       `;;;;;;;;;;;;;;; ;;;; '
#           ''''''''''''' ;;;.
#                .;;;.    `;;;.
#               ;;;; '     ;;;;
#               ;;;;,,,..,;;;;;
#               `;;;;;;;;;;;;;'
#                 `;;;;;;;;;
# """)