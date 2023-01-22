import Dragon
import Fairy
import Story
import random

state = 1

while (state > 0):
    if (state == 1):
        msg1 = Story.story1()
        msg1.show()

        text = input()

        if (text == "y"):
            state = state + 1

    if (state == 2):
        msg1 = Story.story2()
        msg1.show()

        text2 = input()

        if (text2 == "y"):
            state = state + 1

    if (state == 3):
        msg1 = Story.story3()
        msg1.show()

        text3 = input()

        if (text3 == "y"):
            state = state + 1

    if (state == 4):
        msg1 = Story.story4()
        msg1.show()

        text4 = input()

        if (text4 == "1"):
            attack = Dragon.attack
            defense = Dragon.defense
            magic = Dragon.magic
            state = state + 1
        
        if (text4 == "2"):
            attack = Fairy.attack
            defense = Fairy.defense
            magic = Fairy.magic
            state = state + 1

    if (state == 5):
        msg1 = Story.story5()
        msg1.show()

        text5 = input()

        if (text5 == "1"):
            attack = attack + 1
            state = state + 2
            print("You select the Rock, off we go!")
        
        if (text5 == "2"):
            defense = defense + 1
            state = state + 2
            print("You select the Wooden Board, off we go!")

        if (text5 == "3"):
            magic = magic + 1
            state = state + 2
            print("You select the notebook, off we go!")
        
        if (text5 == "4"):
            state = state + 2
            print("You select nothing, off we go!")

    if (state == 7):
        msg1 = Story.story7()
        msg1.show()

        text7 = input()

        if (text7 == "y"):
            state = state + 1

    if (state == 8):
        msg1 = Story.story8()
        msg1.show()

        enemyHP = 10
        health = 10
        
        while (enemyHP > 0) & (health > 0):
            print("1. Roll")
            text8 = input()
            if (text8 == "1"):
                hit = random.randrange(1, 7)
                print("You rolled a: ", hit)
                print("2. Reroll?")
                text8 = input()

                if (text8 == "2"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 1 
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 1
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        state = state + 1

        if (health < 10) & (health >= 8):
            attack = attack + 1

        if (health >= 1) & (health <= 3):
            attack = attack - 1

        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0
        

    if (state == 9):
        msg1 = Story.story9()
        msg1.show()
        print(" [AT: ", attack, "]")
        print("[Press y to continue]")
        text9 = input()

        if (text9 == "y"):
            state = state + 1     

    if (state == 10):
        msg1 = Story.story10()
        msg1.show()

        enemyHP = 10
        health = 10
        
        while (enemyHP > 0) & (health > 0):
            print("1. Roll")
            text10 = input()
            if (text10 == "1"):
                hit = random.randrange(1, 7)
                print("You rolled a: ", hit)
                print("2. Reroll?")
                text10 = input()

                if (text10 == "2"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    enemyHP = enemyHP - (hit)*(1.5**defense)
                    health = health - 1 
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    enemyHP = enemyHP - (hit)*(1.5**defense)
                    health = health - 1
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        state = state + 1

        if (health < 10) & (health >= 8):
            defense = defense + 1

        if (health >= 1) & (health <= 3):
            defense = defense - 1

        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0

    if (state == 11):
        msg1 = Story.story11()
        msg1.show()
        print(" [DF: ", defense, "]")
        print("[Press y to continue]")
        text11 = input()

        if (text11 == "y"):
            state = state + 1 

    if (state == 12):
        msg1 = Story.story12()
        msg1.show()

        enemyHP = 10
        health = 10
        
        while (enemyHP > 0) & (health > 0):
            print("1. Roll")
            text12 = input()
            if (text12 == "1"):
                hit = random.randrange(1, 7)
                print("You rolled a: ", hit)
                print("2. Reroll?")
                text12 = input()

                if (text12 == "2"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 1 
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 1
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        state = state + 1

        if (health < 10) & (health >= 8):
            magic = magic + 1

        if (health >= 1) & (health <= 3):
            magic = magic - 1

        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0

    if (state == 13):
        msg1 = Story.story13()
        msg1.show()
        print(" [MG: ", magic, "]")
        print("[Press y to continue]")
        text13 = input()

        if (text13 == "y"):
            state = state + 1 

    if (state == 14):
        msg1 = Story.story14()
        msg1.show()

        enemyHP = 15
        health = 10
        
        while (enemyHP > 0) & (health > 0):
            print("1. Attack")
            print("2. Magic")
            text14 = input()
           
            if (text14 == "1"):
                hit = random.randrange(1, 7)
                print("You rolled a: ", hit)
                print("3. Reroll?")
                text14 = input()

                if (text14 == "3"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    enemyHP = enemyHP - (hit)*(1.5**attack)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
            if (text14 == "2"):
                hit = random.randrange(1, 7)
                print("You rolled a: ", hit)
                print("3. Reroll?")
                text14 = input()

                if (text14 == "3"):
                    hit = random.randrange(1, 7)
                    print("You rolled a: ", hit)

                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")
            
                else:
                    enemyHP = enemyHP - (hit)*(1.5**magic)
                    health = health - 2**(-defense)
                    print("You: ", health, " HP")
                    print("Enemy: ", enemyHP, " HP")

        state = state + 1

        if (health <= 0):
            msg1 = Story.death()
            msg1.show()
            state = 0

    if (state == 15):
        msg1 = Story.story15()
        msg1.show()
        print("Final Stats: [AT: ", attack, " | DF: ", defense, " | MG: ", magic, "]")
        state = 0
