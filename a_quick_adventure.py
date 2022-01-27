# ***************************************************** #
#                                                       #
#     Code Block 1                                      #
#     Complete the Information Comment Block            #
#                                                       #
# ***************************************************** #
"""

    Author: John Velis
    Created: 1/19/2022
    Modified: 1/26/2022
    Title: A Quick Adventure
    Notes:
     1) This application is designed to demonstrate the use of conditionals to 
        control the flow of the application and user feedback.
     2) Variables are declared and initialized in a single location for clarity. A
        common variable (user_response) will be used for all user action choices.
     3) The code uses significant commenting to help locate and explain coding examples.
     4) All user responses are assumed to be in the correct format and no user input
        validation is performed.
     5) If a user enters an invalid response, the "else" code block will be executed.
     6) A left margin is applied to all output using a constant (left_margin) to for readability.
    
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
#     Setup the Game                                    #
#     Declare and Initialize Variables and Constants    #
#                                                       #
# ***************************************************** #
left_margin = '  '
user_response = ''
#
# Setup initial game values.
#
gold_value = 20
health = 100
have_life_potion = False
have_sword = False
have_book = False
did_enter = False
is_dead = False

# ***************************************************** #
#                                                       #
#     Code Block 3                                      #
#     Introduce and Play the game                       #
#                                                       #
# ***************************************************** #
print()
print(left_margin + 'This application will take you on an adventure.')
print(left_margin + 'You will explore a dungeon, gather treasure and try to not')
print(left_margin + 'get killed by the many dangers you will encounter.')
sleep(1)

print()
input(left_margin + 'Press the Enter key to continue.') # Pause app for the user.
sleep(1)

print()
player_name = input(left_margin + 'What is your name?') # 
sleep(1)

#
# Note: f-String formatting will be the primary method of formatting strings.
#
print()
print()
print(left_margin + f'Well {player_name}, it is nice to meet you. I am Jorka the Dungeon Master.')
print(left_margin + 'As you move through the dungeon I will describe where you are and give you')
print(left_margin + 'choices for your next action. The choice will be in the square brackets.')
print(left_margin + 'Be sure to type your choice exactly how it appears in the brackets.')
sleep(1)

print()
input(left_margin + 'Press the Enter key to continue.') # Pause app for the user.
sleep(1)

print()
print(left_margin + left_margin + '********************************************')
print(left_margin + left_margin + '*                                          *')
print(left_margin + left_margin + '*         Outside the Dungeon              *')
print(left_margin + left_margin + '*                                          *')
print(left_margin + left_margin + '********************************************')
print()
sleep(2)
print(left_margin + 'You are standing in front of a large, old metal door, maybe 8 feet high.') 
print(left_margin + 'There are strange symbols on the door with a haunting image of a scull near the latch.') 
print(left_margin + 'The latch is rusty and corroded as if not used in decades.') 
print()
user_response = input(left_margin + f'Well {player_name}, do you open the door and enter or just leave [enter/leave].') 
sleep(1)

#
# Player chooses to play the game.
#
if user_response == 'enter':

    did_enter = True # Use this variable at the end of the game.

    #
    # Note: Multiline string used for commenting code
    #
    """
    Location: The Gallery
    NPC: Gorup the Troll
    Treasure: 5 Gold Pieces                        
    Weapons: None
    Potions: None

    """

    print()
    print()
    print(left_margin + left_margin + '********************************************')
    print(left_margin + left_margin + '*                                          *')
    print(left_margin + left_margin + '*         The Gallery                      *')
    print(left_margin + left_margin + '*                                          *')
    print(left_margin + left_margin + '********************************************')
    print()
    sleep(2)
    print(left_margin + 'The latch requires a great deal of force to open, but eventually slides and the door opens.') 
    print(left_margin + 'As you walk through the door, you notice a torch in the corner of what seems to be a large room.') 
    print(left_margin + 'As you walk torward the torch you can see that it is held by a small troll and he speaks.') 
    print(left_margin + '\"My name is Gorup and I am keeper of this world. You are welcome, but beware. Not all of our') 
    print(left_margin + 'dwellers mean you well. Jorka instructed me to give you five gold pieces if you choose to leave.\"') 
    print()
    user_response = input(left_margin + 'Do you continue or leave [continue/leave].?') 
    sleep(1)

    #
    # player takes the gold and continues into the dungeon
    #
    if user_response == 'continue':
        print()
        print()
        print(left_margin + 'Gorup points toward two doors behind him.') 
        print(left_margin + 'One is ornate, guilded with silver and gold.') 
        print(left_margin + 'The other is made up of splintered wood, roughly nailed together.')
        print()
        user_response = input(left_margin + 'Do you choose the ornate or wood door [ornate/wooden]?') 
        sleep(1)

        #
        # player chooses the Ornate Door
        #
        if user_response == 'ornate':
            """
            Location: Mirrored Room
            NPC: None
            Treasure: None                        
            Weapons: None
            Potions: None

            """
            print()
            print()
            print(left_margin + left_margin + '********************************************')
            print(left_margin + left_margin + '*                                          *')
            print(left_margin + left_margin + '*         The Mirrored Room                *')
            print(left_margin + left_margin + '*                                          *')
            print(left_margin + left_margin + '********************************************')
            print()
            print(left_margin + 'Walking through the door you notice the room is brightly lit by a huge') 
            print(left_margin + 'chandelier and the walls are completely covered by mirrors. In the center') 
            print(left_margin + 'of the room a large, crystal pedistle holds a smooth, black onyx box.') 
            print(left_margin + 'A disembodied voice says \"Open the box to end your journey.\"') 
            print(left_margin + 'Walking toward the pedistle you notice a small portal in it, just big')
            print(left_margin + 'enough for you to squeeze through.')
            print()
            user_response = input(left_margin + 'Do you open the box or use the door [box/portal]?') 
            sleep(1)

            if user_response == 'box':
                print()
                print(left_margin + 'Opening the box, you find 50 gold pieces. You quickly fill your pockets')
                print(left_margin + 'with the gold and as you take the last gold piece, a bright, blinding light')  
                print(left_margin + 'is emitted from the box and you feel yourself fade from the room.')
                sleep(2)

                #
                # add gold to player's treasure
                #
                gold_value = gold_value + 50
            
            elif user_response == 'portal':
                #
                # Player looses 20 points of health
                #
                health = health - 20 

                print()
                print(left_margin + 'Climbing through the tight opening for the portal you feel a tingling on your')
                print(left_margin + 'skin and begin to feel a bit sick.')  
                print(left_margin + 'As you exit the portal you begin to feel better, but loose 10 health points.')
                print(left_margin + f'Your health is now at {health} points.')
                sleep(2)

            #
            # Player did not enter a valid response for their choice.
            #
            else:
                print()
                print(left_margin + 'I am afraid I do not understand your response.') 
                sleep(2) 

        #
        # player chooses the Wooden Door
        #
        elif user_response == 'wooden':
            """
            Location: Armory
            NPC: Talmay the Dwarf
            Treasure: 10 Gold Pieces                        
            Weapons: Slayer the Battle Sword 
            Potions: None

            """
            print()
            print()
            print(left_margin + left_margin + '********************************************')
            print(left_margin + left_margin + '*                                          *')
            print(left_margin + left_margin + '*         The Armory                       *')
            print(left_margin + left_margin + '*                                          *')
            print(left_margin + left_margin + '********************************************')
            print()
            print(left_margin + 'The wooden door creaks as you push on it to open. Inside is a small room')
            print(left_margin + 'with a low ceiling. Lit by torch pot along the middle walkway the walls')  
            print(left_margin + 'the walls are covered with all sorts of weapons from knives to swords and') 
            print(left_margin + 'battle axes with various shields hanging on the far wall. You notice one')
            print(left_margin + 'sword, brighter than the rest, nestled in a cradle of silver with the name')
            print(left_margin + '\"The Slayer\" engraved in the hilt. Next to the sword is a bag of 10 gold pieces.')
            print()
            user_response = input(left_margin + 'Before leaving the armory, do you take the sword or the gold [sword/gold]?') 
            sleep(1)

            if user_response == 'sword':
                #
                # add sword to player's inventory
                #
                have_sword = True

                print(left_margin + 'You take the sword and tie it to your belt.')

            elif user_response == 'gold':
                #
                # add gold to player's treasure
                #
                gold_value = gold_value + 10

                print(left_margin + f'You pocket the gold and note that you now have {gold_value} gold pieces.')

            #
            # Player did not enter a valid response of what to take.
            #
            else:
                print()
                print(left_margin + 'I am afraid I do not understand your response.') 
                sleep(2)  

        #
        # Player did not enter a valid response for the room.
        #
        else:
            print()
            print(left_margin + 'I am afraid I do not understand your response.') 
            sleep(2)  

        print()
        input(left_margin + 'Press the Enter key to continue.') # Pause app for the user.
        sleep(1)

        """
        Location: Dining Hall
        NPC: Minotaur
        Treasure: 50 Gold Pieces                       
        Weapons: None
        Potions: Distilled Nectar of the Broadroot Tree

        """   
        print()
        print()
        print(left_margin + left_margin + '********************************************')
        print(left_margin + left_margin + '*                                          *')
        print(left_margin + left_margin + '*         Dining Hall                      *')
        print(left_margin + left_margin + '*                                          *')
        print(left_margin + left_margin + '********************************************')
        print()
        print(left_margin + 'You now find yourself in a large hall, well lit by candles and warmed by a huge')
        print(left_margin + 'fireplace at one end. A long table lined with chairs sets in the middle of the')  
        print(left_margin + 'room. All chairs are empty save one where a old, gnarly minotaur sits, head down.') 
        print(left_margin + 'Walking closer, you watch as the minotaur stands and unsheathes a sword.')
        print(left_margin + 'It looks at you and asks what you have brought.')

        if have_sword:
            print()
            print(left_margin + 'You remember the sword in your belt and put a hand on it.')
            print()
            user_response = input(left_margin + 'Do you draw your sword and attach the minotaur [yes/no]?') 
            sleep(1)

            #
            # Player attacks the minotaur
            #
            if user_response == 'yes':  
                #
                # Player looses 20 points of health
                #
                health = health - 20 

                print()
                print(left_margin + 'The minotaur leaps at you and with one swift blow sends you flying to the ground.')
                print(left_margin + '\"You must leave now!\" shouts the minotaur and raise her sword again.')
                print(left_margin + f'You loose 20 points of health and are now at {health} points.')
                sleep(1)

            #
            # Player did not attacks the minotaur
            #
            elif user_response == 'no': 
                print()
                print(left_margin + 'You remove your hand from your sword and the minotaur smiles.')
                print(left_margin + '\"Wise choice Little One. I am sure I would have bested you on this day.\" ')
                print()
                sleep(1)

            #
            # Player did not enter a valid response about drawing their sword.
            #
            else:
                print()
                print(left_margin + 'I am afraid I do not understand your response.') 
                sleep(2)

        print()
        print(left_margin + 'You remember the gold you carry and wonder if it would please the minotaur.')
        print()
        user_response = input(left_margin + 'Do you offer the minotaur 10 gold pieces [yes/no]?') 
        sleep(1)

        #
        # Player offers gold to minotaur.
        #
        if user_response == 'yes':
            #
            # Subtract from player's treasure
            #
            gold_value = gold_value - 10

            #
            # Add potion to player's inventory.
            #
            have_life_potion = True 

            print(left_margin + 'The minotaur is pleased and offers you a vile containing a purple, sticky liquid.')
            print(left_margin + '\"Keep that close at hand. The potion will heal most anything. You will find it useful')  
            print(left_margin + 'in your journey I am quite sure.\"')

        #
        # Player did not pay the minotaur
        #
        elif user_response == 'no': 
            print()
            print(left_margin + 'You say nothing and the minotaur, looking very displeased waves you on your way.')
            print()
            sleep(1)

        #
        # Player did not enter a valid response about paying the minotaur.
        #
        else:
            print()
            print(left_margin + 'I am afraid I do not understand your response.') 
            sleep(2) 

        print()
        input(left_margin + 'Press the Enter key to continue.') # Pause app for the user.
        sleep(1)                

        """
        Location: The Great Study
        NPC: Alitoria the Elf
        Treasure: 25 Gold Pieces                       
        Weapons: None
        Potions: None
        Item: Book of Wisdom

        """   
        print()
        print()
        print(left_margin + left_margin + '********************************************')
        print(left_margin + left_margin + '*                                          *')
        print(left_margin + left_margin + '*         The Great Study                  *')
        print(left_margin + left_margin + '*                                          *')
        print(left_margin + left_margin + '********************************************')
        print()
        print(left_margin + 'Walking on you enter a room lined by shelves of old books. The walls')
        print(left_margin + 'are covered with paintings of grand humans and elves. Sitting at one of the')  
        print(left_margin + 'wooden desks under a painting of a tall elf dressed blue satin is a small') 
        print(left_margin + 'elvin girl. You introduce yourself and she looks up. \"Did Gorup send you to find me?\"')
        print(left_margin + 'You nod and she asks if you have five gold pieces for her.')   
        print()  
        user_response = input(left_margin + 'Do you offer the elf 5 gold pieces [yes/no]?') 
        sleep(1)

        if user_response == 'yes':
            #
            # Subtract from the players treasure.
            #
            gold_value = gold_value - 5

            #
            # Add book to player's inventory.
            #
            have_book = True

            print()
            print(left_margin + 'Reaching into your pocket, you pull out five gold pieces and give them')
            print(left_margin + 'to the elf. She is very pleased, stands and pulls a leather bound book') 
            print(left_margin + 'from one of the shelves and hands it to you.') 
            print(left_margin + 'Taking the book, you thank her. She raises both hands, waving them in')                          
            print(left_margin + 'circular motions and the room begins to fade as you feel yourself drawn')  
            print(left_margin + 'into the darkness.')  
            sleep(1)

        elif user_response == 'no':
            #
            # Set the Boolean variable for the player's death.
            #
            is_dead = True

            print()
            print(left_margin + 'Keeping the gold in your pockets, you apologize and say that you have nothing')
            print(left_margin + 'for her. She looks at you glaringly, draws a dagger from her cloak and thrusts') 
            print(left_margin + 'it into your heart, killing you immediately.') 
            print()
            print(left_margin + 'The room begins to fade as you feel yourself drawn')  
            print(left_margin + 'into the darkness.') 
            sleep(1)
        
        #
        # Player did not enter a valid response
        #
        else:
            print()
            print(left_margin + 'I am afraid I do not understand your response.') 
            sleep(2)

        #
        # The game is complete and the player leaves the dungeon. (Code Block 4)
        #


    #
    # Player leaves the dungeon. (Code Block 4)
    #
    elif user_response == 'leave':
        #
        # add the gold to the player's treasure
        #
        gold_value = gold_value + 5   

        print()
        print(left_margin + 'You pocket the five gold pieces and turn to walk out the door.') 
        sleep(2)


    #
    # Player did not enter a valid response and leaves the dungeon. (Code Block 4)
    #
    else:
        print()
        print(left_margin + 'I am afraid I do not understand your response.') 
        sleep(2)
#
# Player chose to not enter the dungeon.  (Code Block 4)
#
else:
    did_enter = False

print()
input(left_margin + 'Press the Enter key to continue.') # Pause app for the user.
sleep(1)

# ***************************************************** #
#                                                       #
#     Code Block 4                                      #
#     Process the End of the Game                       #
#                                                       #
# ***************************************************** #

print()

#
# Player entered the dungeon
#
if did_enter:
    print()
    print(left_margin + left_margin + '********************************************')
    print(left_margin + left_margin + '*                                          *')
    print(left_margin + left_margin + '*         Outside the Dungeon              *')
    print(left_margin + left_margin + '*                                          *')
    print(left_margin + left_margin + '********************************************')
    print()
    print()
    print(left_margin + 'You awaken outside the first door. Jorka stands over you.') 
    sleep(1)
    print()

    #
    # Player died.
    #
    if is_dead:
        print()
        print(left_margin + f'Well {player_name}, it appears you did not survive my dungeon.')
        print()

        if gold_value > 0:
            print(left_margin + f'I will take back your {gold_value} gold pieces.') 
            print()
            sleep(1)

        if have_sword:
            print(left_margin + 'I will take back your sword as you will not be needing it anymore.') 
            print()
            sleep(1)

        if have_life_potion:
            print(left_margin + 'I see you have the minotaur\'s potion which has restored your life.')
            print(left_margin + 'You leave my dungeon alive today. Haaaa haaa!')
            print()

        print(left_margin + f'You are free to go {player_name}, but come back again when you are better prepared.') 
        sleep(1)
    
    #
    # Player survived.
    #
    else:
        print()
        print(left_margin + f'Well {player_name}, it appears you survived my dungeon.')
        print()

        if gold_value > 50 and have_book:
            print(left_margin + f'Not a bad take coming home with {gold_value} gold pieces and the elvin book, eh?')
            print() 
            sleep(1)
        elif gold_value > 50:
            print(left_margin + f'Not a bad take coming home with {gold_value} gold pieces eh?')
            print() 
            sleep(1)
        elif gold_value > 25:
            print(left_margin + f'You could have done better than coming home with {gold_value} gold pieces eh?')
            print() 
            sleep(1)
        else:
            print(left_margin + f'It appears you will be leaving with {gold_value} gold pieces')
            print() 
            sleep(1)

        if have_sword:
            print(left_margin + 'I will take back your sword as you will not be needing it anymore.') 
            print()
            sleep(1)

        if have_life_potion:
            print(left_margin + 'You may keep the Life Potion if you like, since it was a gift from the minotaur.') 
            print()
            sleep(1)

        print(left_margin + f'You are free to go {player_name}, and come back when you want to play again.') 
        print()
        sleep(1)

#
# Player did not enter the dungeon.
#
else: 
    print()
    print()
    print(left_margin + f'I am sorry you did not want to play today {player_name}, but come back again if your wish.') 
    print()
    sleep(1)    

print()
input(left_margin + 'Press the Enter key to exit.') # pause app so the user can read the final comments

