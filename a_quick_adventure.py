# ***************************************************** #
#                                                       #
#     Code Block 1                                      #
#     Complete the Information Comment Block            #
#                                                       #
# ***************************************************** #
"""

    Author: John Velis
    Created: 1/19/2022
    Modified: 
    Title: A Quick Adventure
    Notes:
     1) This application is designed to demonstrate the use of conditionals to 
        control the flow of the application and user feedback.
     2) Variables are declared and initialized in a single location for clarity. A
        common variable (user_response) will be used for all user action choices.
     3) The code uses significant commenting to help locate and explain coding examples.
     3) All user responses are assumed to be in the correct format and no user input
        validation is performed.
     4) A left margin is applied to all output using a constant (left_margin) to for readability.
    
"""

# ***************************************************** #
#                                                       #
#     Import Python Modules                             #
#                                                       #
# ***************************************************** #
from time import sleep

# ***************************************************** #
#                                                       #
#     Code Block 2                                      #
#     Declare and Initialize Variables and Constants    #
#     Note: Variables can also be declared when they    #
#           first assigned a value.                     #
#                                                       #
# ***************************************************** #
left_margin = '  '
user_response = ''



# ***************************************************** #
#                                                       #
#     Code Block 3                                      #
#     Introduce Yourself and the Application            #
#                                                       #
# ***************************************************** #
print(left_margin + 'Hello, my name is Bonzo.')
sleep(1)
print()
print(left_margin + 'This application will take you on an adventure.')
print(left_margin + 'You will explore a dungeon, gather treasure and try to not')
print(left_margin + 'get killed by the many dangers you will encounter.')
sleep(1)
print()
input(left_margin + 'Press the Enter key to continue.') # pause app for the user

print()
player_name = input(left_margin + 'What is your name?') # 
sleep(1)

#
# Note: f-String formatting will be the primary method of formatting strings.
#
print(left_margin + f'Well {player_name}, it is nice to meet you. I am Jorka the Dungeon Master.')
print(left_margin + 'As you move through the dungeon I will describe where you are and give you')
print(left_margin + 'choices for your next action. The choice will be in the square brackets.')
print(left_margin + 'Be sure to type your choice exactly how it appears in the brackets.')
sleep(1)
print()
input(left_margin + 'Press the Enter key to continue.') # pause app for the user

# ***************************************************** #
#                                                       #
#     Code Block 4                                      #
#     Ask User to Continue or Exit                      #
#                                                       #
# ***************************************************** #
print()
print(left_margin + 'You are standing in front of a large, old metal door, maybe 8 feet high.') 
print(left_margin + 'You are standing in front of a large, old metal door, maybe 8 feet high.') 
user_response = input(left_margin + f'Well {player_name}, do you open the door and enter or leave [enter/leave].') 
sleep(1)

#
# Use an if/else block to give the user an opportunity to exit the app.
#

if user_response == 'enter':

    # ***************************************************** #
    #                                                       #
    #     Code Block 5                                      #
    #     Start the Game                                    #
    #                                                       #
    # ***************************************************** #
    print()

else:

    # ***************************************************** #
    #                                                       #
    #     Code Block 6                                      #
    #     Thank the User and Exit the App                   #
    #                                                       #
    # ***************************************************** #
    print()
    print(left_margin + 'That\'s too bad, because I really like to make stories with people.')
    print(left_margin + 'Thanks you for trying my application and have a nice day.')
    sleep(1)
    print()
    input(left_margin + 'Press the Enter key to exit.') # pause app so the user can read the final comments

