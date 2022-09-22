import cowsay
import os
import schedule
import time
import getch
# import PIL

# from PIL import Image

# # ascii characters used to build the output text
# ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# # resize image according to a new width
# def resize_image(image, new_width=100):
#     width, height = image.size
#     ratio = height/width
#     new_height = int(new_width * ratio)
#     resized_image = image.resize((new_width, new_height))
#     return(resized_image)

# # convert each pixel to grayscale
# def grayify(image):
#     grayscale_image = image.convert("L")
#     return(grayscale_image)
    
# # convert pixels to a string of ascii characters
# def pixels_to_ascii(image):
#     pixels = image.getdata()
#     characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
#     return(characters)    

# def main(new_width=100):
#     # attempt to open image from user-input
#     path = input("Enter a valid pathname to an image:\n")
#     try:
#         image = PIL.Image.open(path)
#     except:
#         print(path, " is not a valid pathname to an image.")
#         return
  
#     # convert image to ascii    
#     new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
#     # format
#     pixel_count = len(new_image_data)  
#     ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
#     # print result
#     print(ascii_image)
    
#     # save result to "ascii_image.txt"
#     with open("ascii_image.txt", "w") as f:
#         f.write(ascii_image)
 
# # run program
# main()
music_img = """

               .....
           .;;;;;;;;;,
          ;;;'    `;;;,
         ;;;'      `;;;
         ;;;        ;;;
         ;;;.      ;;;'
         `;;;.    ;;;'
          `;;;.  ;;;'
           `;;',;;'
            ,;;;'
         ,;;;',;' ...,,,,...
      ,;;;'    ,;;;;;;;;;;;;;;,
   ,;;;'     ,;;;;;;;;;;;;;;;;;;,
  ;;;;'     ;;;',,,   `';;;;;;;;;;
 ;;;;,      ;;   ;;;     ';;;;;;;;;
;;;;;;       '    ;;;      ';;;;;;;
;;;;;;            .;;;      ;;;;;;;
;;;;;;,            ;;;;     ;;;;;;'
 ;;;;;;,            ;;;;   .;;;;;'
  `;;;;;;,           ;;;; ,;;;;;'
   `;;;;;;;,,,,,,,,,, ;;;; ;;;'
      `;;;;;;;;;;;;;;; ;;;; '
          ''''''''''''' ;;;.
               .;;;.    `;;;.
              ;;;; '     ;;;;
              ;;;;,,,..,;;;;;
              `;;;;;;;;;;;;;'
                `;;;;;;;;;
"""


# print(ascii)

cowsay.stegosaurus('General Knowledge')
# # cowsay.koala('General Knowledge')

# os.system('cmatrix 9') 

# def matrix():
#   
 



print("""
        _____!
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-:
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____. '
""")

/|
                                     |\|
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                     |||
                                  ~-[{o}]-~
                                     |/|
                                     |/|
             ///~`     |\\_          `0'         =\\\\         . .
            ,  |='  ,))\_| ~-_                    _)  \      _/_/|
           / ,' ,;((((((    ~ \                  `~~~\-~-_ /~ (_/\
         /' -~/~)))))))'\_   _/'                      \_  /'  D   |
        (       (((((( ~-/ ~-/                          ~-;  /    \--_
         ~~--|   ))''    ')  `                            `~~\_    \   )
             :        (_  ~\           ,                    /~~-     ./
              \        \_   )--__  /(_/)                   |    )    )|
    ___       |_     \__/~-__    ~~   ,'      /,_;,   __--(   _/      |
  //~~\`\    /' ~~~----|     ~~~~~~~~'        \-  ((~~    __-~        |
((()   `\`\_(_     _-~~-\                      ``~~ ~~~~~~   \_      /
 )))     ~----'   /      \                                   )       )
  (         ;`~--'        :                                _-    ,;;(
            |    `\       |                             _-~    ,;;;;)
            |    /'`\     ;                          _-~          _/
           /~   /    |    )                         /;;;''  ,;;:-~
          |    /     / | /                         |;;'   ,''
          /   /     |  \\|                         |   ,;(    -Tua Xiong
        _/  /'       \  \_)                   .---__\_    \,--._______
       ( )|'         (~-_|                   (;;'  ;;;~~~/' `;;|  `;;;\
        ) `\_         |-_;;--__               ~~~----__/'    /'_______/
        `----'       (   `~--_ ~~~;;------------~~~~~ ;;;'_/'
                     `~~~~~~~~'~~~-----....___;;;____---~~