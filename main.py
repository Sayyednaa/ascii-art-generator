from art import *

import os
print("<==============ASCII Art Generator. ==========>\n")
print("Coded By:\n")
Art=text2art("Abdul Ali",font='block',chr_ignore=True) # Return ASCII text with block font
print(Art)
user = ''
while user != '~':
    user = input("Enter The Input or ~ to Quit:\n")

    if user =='~':
        
        exit()
    Art=text2art(user,font='block',chr_ignore=True) # Return ASCII text with block font
    file = open(user +".txt","w+")
    file.write(Art)
    print(Art)

