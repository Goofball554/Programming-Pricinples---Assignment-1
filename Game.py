import Dragon
import Fairy
import Story
import random

def GameExplanation(argument):
    """
    This module contains all the logic for the game.

    It takes user input to change states (go from one paragraph of text to the next).

    It also contains the random dice roll code that works as the player's attack. 
    """

    return argument


# State is used to move between one paragraph of text to the next and to progress in the challenges. 
state = 1

while (state > 0):
    if (state == 1):

        # Displays the first paragraph of the story
        msg1 = Story.story1()
        msg1.show()

        #Asks the user for input
        text = input()

        #If the user inputs "y", the state is increased and the next state executes
        if (text == "y"):
            state = state + 1

    if (state == 2):

        #Displays the second paragraph of the story
        msg1 = Story.story2()
        msg1.show()

        #Asks the user for input
        text2 = input()

        #If the user input "y", the state is increased and the next state executes
        if (text2 == "y"):
            state = state + 1

    if (state == 3):

        #Displays the third paragraph of the story
        msg1 = Story.story3()
        msg1.show()

        #Asks the user for input
        text3 = input()

        #If the user input "y", the state is increased and the next state executes
        if (text3 == "y"):
            state = state + 1

    if (state == 4):

        #Displays the fourth paragraph of the story
        msg1 = Story.story4()
        msg1.show()

        #Asks the user for input
        text4 = input()

        #If the user input "1", the attack, defense, and magic attributes are assigned based on Dragon.py
        #The state is then increased and the next state executes
        if (text4 == "1"):
            attack = Dragon.attack
            defense = Dragon.defense
            magic = Dragon.magic
            state = state + 1
        
        #If the user input "2", the attack, defense, and magic attributes are assigned based on Fairy.py
        #The state is then increased and the next state executes
        if (text4 == "2"):
            attack = Fairy.attack
            defense = Fairy.defense
            magic = Fairy.magic
            state = state + 1

    if (state == 5):

        #Displays the fifth paragraph of the story 
        msg1 = Story.story5()
        msg1.show()

        #Asks the user for input
        text5 = input()

        #If the user input "1", the rock is selected and the attack attribute is incereased by 1
        #The state then increases by 2 (skiping the missing state 6) and the next state executes
        if (text5 == "1"):
            attack = attack + 1
            state = state + 2
            print("You select the Rock, off we go!")
        
        #If the user input "2", the rock is selected and the defense attribute is incereased by 1
        #The state then increases by 2 (skiping the missing state 6) and the next state executes
        if (text5 == "2"):
            defense = defense + 1
            state = state + 2
            print("You select the Wooden Board, off we go!")

        #If the user input "3", the notesbook is selected and the magic attribute is incereased by 1
        #The state then increases by 2 (skiping the missing state 6) and the next state executes
        if (text5 == "3"):
            magic = magic + 1
            state = state + 2
            print("You select the notebook, off we go!")
        
        #If the user input "4", nothing is selected
        #The state then increases by 2 (skiping the missing state 6) and the next state executes
        if (text5 == "4"):
            state = state + 2
            print("You select nothing, off we go!")

#STATE 6 IS MISSING DUE TO FAULTY COUNTING AND DEBUGGING ISSUES

    if (state == 7):
        
        #Displays the seventh paragraph of the story
        msg1 = Story.story7()
        msg1.show()

        #Asks the user for input
        text7 = input()

        #If the user input "y", the state is increased and the next state executes
        if (text7 == "y"):
            state = state + 1

    if (state == 8):

        #Displays the eighth paragraph of the story 
        msg1 = Story.story8()
        msg1.show()

        #Sets the enemy's HP to 10
        #Sets the player's HP to 10
        enemyHP = 10
        health = 10
        
        def Fight1Explanation(argument):
            """
            This while loop contains all the logic for the fight. 

            It asks the user to input "1" to roll the dice and then prints out the result. 

            It then asks the user if they would like to reroll by pressing "2".

            Damage is then deducted from the enemy based ont he dice roll and an attack attribute multiplier.  
            """

            return argument

        while (enemyHP > 0) & (health > 0):
            print("1. Roll")

            #Asks the user for input
            text8 = input()

            #If the user inputs "1", the program rolls a dice
            if (text8 == "1"):
                hit = random.randrange(1, 7)

                #Prints out the roll of the dice
                print("You rolled a: ", hit)
                
                #Asks the user if they would like to reroll the dice
                print("2. Reroll?")
                text8 = input()

                #If the user inputs "2", the program rerolls the dice
                if (text8 == "2"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 1 
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 1
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        #Once the enemey's HP reaches 0, the state is increased and the next state executes
        state = state + 1

        #If the player's health is between 8 and 10 (critical win), their attack attribute increases by 1
        if (health < 10) & (health >= 8):
            attack = attack + 1


        #If the player's health is between 1 and 3 (critical loss), their attack attribute decreases by 1
        if (health >= 1) & (health <= 3):
            attack = attack - 1

        #If the player's health reaches 0, the GAME over message displays
        #State is set to 0 to stop the while loop
        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0
        

    if (state == 9):

        #Displays the ninth paragraph of the story and the player's new attack attribute
        msg1 = Story.story9()
        msg1.show()
        print(" [AT: ", attack, "]")
        print("[Press y to continue]")

        #Asks the user for input
        text9 = input()

        #If the user input "y", the state is increased and the next state executes
        if (text9 == "y"):
            state = state + 1     

    if (state == 10):

        #Displays the tenth paragraph of the story
        msg1 = Story.story10()
        msg1.show()

        #Sets the enemy's HP to 10
        #Sets the player's HP to 10
        enemyHP = 10
        health = 10

        def Fight2Explanation(argument):
            """
            This while loop contains all the logic for the fight. 

            It asks the user to input "1" to roll the dice and then prints out the result. 

            It then asks the user if they would like to reroll by pressing "2".

            Damage is then deducted from the enemy based on the dice roll and an defense attribute multiplier.  
            """

            return argument
        
        while (enemyHP > 0) & (health > 0):
            print("1. Roll")

            #Asks the user for input 
            text10 = input()

            #If the user inputs "1", the program rolls a dice
            if (text10 == "1"):
                hit = random.randrange(1, 7)

                #Prints out the roll of the dice
                print("You rolled a: ", hit)
                
                #Asks the user if they would like to reroll the dice
                print("2. Reroll?")
                text10 = input()

                #If the user inputs "2", the program rerolls the dice
                if (text10 == "2"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**defense)
                    health = health - 1 
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**defense)
                    health = health - 1
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        #Once the enemey's HP reaches 0, the state is increased and the next state executes
        state = state + 1

        #If the player's health is between 8 and 10 (critical win), their defense attribute increases by 1
        if (health < 10) & (health >= 8):
            defense = defense + 1

        #If the player's health is between 1 and 3 (critical loss), their attack attribute decreases by 1
        if (health >= 1) & (health <= 3):
            defense = defense - 1

        #If the player's health reaches 0, the GAME over message displays
        #State is set to 0 to stop the while loop
        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0

    if (state == 11):
        
        #Displays the eleventh paragraph of the story and the player's new defense attribute
        msg1 = Story.story11()
        msg1.show()
        print(" [DF: ", defense, "]")
        print("[Press y to continue]")

        #Asks the user for input
        text11 = input()

        #If the user input "y", the state is increased and the next state executes
        if (text11 == "y"):
            state = state + 1 

    if (state == 12):

        #Displays the twelveth paragraph of the story
        msg1 = Story.story12()
        msg1.show()

        #Sets the enemy's HP to 10
        #Sets the player's HP to 10
        enemyHP = 10
        health = 10
        
        def Fight3Explanation(argument):
            """
            This while loop contains all the logic for the fight. 

            It asks the user to input "1" to roll the dice and then prints out the result. 

            It then asks the user if they would like to reroll by pressing "2".

            Damage is then deducted from the enemy based on the dice roll and an magic attribute multiplier.  
            """

            return argument

        while (enemyHP > 0) & (health > 0):
            print("1. Roll")

            #Asks the user for input
            text12 = input()

            #If the user inputs "1", the program rolls a dice
            if (text12 == "1"):
                hit = random.randrange(1, 7)

                #Prints out the roll of the dice
                print("You rolled a: ", hit)

                #Asks the user if they would like to reroll the dice
                print("2. Reroll?")
                text12 = input()

                #If the user inputs "2", the program rerolls the dice
                if (text12 == "2"):

                    #Enemy and Player HP is deducted accordingly
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 1 
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 1
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        #Once the enemey's HP reaches 0, the state is increased and the next state executes
        state = state + 1

        #If the player's health is between 8 and 10 (critical win), their magic attribute increases by 1
        if (health < 10) & (health >= 8):
            magic = magic + 1

        #If the player's health is between 1 and 3 (critical loss), their magic attribute decreases by 1
        if (health >= 1) & (health <= 3):
            magic = magic - 1

        #If the player's health reaches 0, the GAME over message displays
        #State is set to 0 to stop the while loop
        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0

    if (state == 13):

        #Displays the thirteenth paragraph of the story and the player's new magic attribute
        msg1 = Story.story13()
        msg1.show()
        print(" [MG: ", magic, "]")
        print("[Press y to continue]")

        #Asks the user for input
        text13 = input()

        #If the user input "y", the state is increased and the next state executes
        if (text13 == "y"):
            state = state + 1 

    if (state == 14):
        msg1 = Story.story14()
        msg1.show()

        #Sets the enemy's HP to 15
        #Sets the player's HP to 10
        enemyHP = 15
        health = 10
        
        def BossFightExplanation(argument):
            """
            This while loop contains all the logic for the fight. 

            It asks the user to input "1" to roll the dice and use their attack attribute
            or "2" to roll the dice and use their magic attribute, and then prints out the result. 

            It then asks the user if they would like to reroll by pressing "3".

            Damage is then deducted from the enemy based on the dice roll and the attribute multiplier selected.

            Damage taken by the player is mupltiplied by their defense attribute. 
            """

            return argument

        while (enemyHP > 0) & (health > 0):
            print("1. Attack")
            print("2. Magic")

            #Asks the user for input
            text14 = input()
           
           #If the user inputs "1" the program rolls a dice
            if (text14 == "1"):
                hit = random.randrange(1, 7)
                print("You rolled a: ", hit)

                #Asks the user if they would like to reroll the dice
                print("3. Reroll?")
                text14 = input()

                if (text14 == "3"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
            #If the user inputs "2" the program rolls a dice
            if (text14 == "2"):
                hit = random.randrange(1, 7)
                print("You rolled a: ", hit)
                print("3. Reroll?")
                text14 = input()

                #Asks the user if they would like to reroll the dice
                if (text14 == "3"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    #Enemy and Player HP is deducted accordingly
                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        #Once the enemey's HP reaches 0, the state is increased and the next state executes
        state = state + 1

        #If the player's health reaches 0, the GAME over message displays
        #State is set to 0 to stop the while loop
        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0

    if (state == 15):
    
        #Prints the final vicotry message and sets the state to 0 to stop the while loop
        msg1 = Story.story15()
        msg1.show()
        print("Final Stats: [AT: ", attack, " | DF: ", defense, " | MG: ", magic, "]")
        state = 0
