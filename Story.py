import Game.py

class story1:
    def show(self):
        msg1 = "Welcome to Dreamland."
        msg2 = "Once a land full of life and luscious plants, now a barren wasteland. Nothing grows, nothing thrives, many have packed up their things and ventured elsewhere. [Press y to continue]"
        print(msg1) 
        print(msg2)

class story2:
    def show(self):
        msg1 = "For the war of dragons and faires has dragged on for centuries. Neither able to overcome the forces of the other and out and end to the fightibng. And so we sit at a stalemate. [Press y to continue]"
        print(msg1)

class story3:
    def show(self):
        msg1 = "Both sides have chosen to send their greatest warrior to Mount Jade, to leave the way in the nands of fate, and collect the EMERALD OF OMNIPOTENCE. Once collected the fighting will cease and peace will return to Dreamland. [Press y to continue]"
        print(msg1)

class story4:
    def show(self):
        msg1 = "So brave warrior, who's side are you on?"
        msg2 = "1. Dragon [HP: 10 | AT: 2 | DF: -2 | MG: 0]"
        msg3 = "My heart burns witht he flames of a thousand suns and my eyes glow with the power of a million moons."
        msg4 = "2. Fairy [HP: 10 | AT: -1 | DF: -1 | MG: 2]"
        msg5 = "My wings can carry me accross the silver winds of the universe and my magic can break even the strongest of minds."
        print(msg1)

        print("")

        print(msg2)
        print(msg3)
        
        print("")

        print(msg4)
        print(msg5)

class story5:
    def show(self):
        msg1 = "Before you embark, and elder walks up to you holding 3 items and offers you one. Which do you take?"
        msg2 = "1. Rock [AT + 1]"
        msg3 = "2. Wooden Board [DF + 1]"
        msg4 = "3. Notebook [MG + 1]"
        msg5 = "4. None"
        print(msg1)

        print("")

        print(msg2)
        print(msg3)
        print(msg4)
        print(msg5)



class story7:
    def show(self):
        msg1 = "There are 3 challenges that stand in your way to Mount Jade, a test of strenth, a test of endurance, and a test of mana. The first challenge that lies before you is the test of strength. [Press y to continue]"
        print(msg1)

class story8:
    def show(self):
        msg1 = "A goblin [HP: 10] stands before you. I am the guardian of strength! it screams. Bow before me!"
        msg2 = "On each turn you will roll a dice to determine how much HP you take from your enemy. You will have one chance to reroll. The enemy will then deal 1 HP of damage back. [Press y to continue]"
        print(msg1)

        print("")

        print(msg2)

class story9:
    def show(self):
        msg1 = "You drag yourself from the battle bleeding and broken, but your spirit unwavering. Ready to take on the next challenge."
        msg2 = "[AT: ", Game.modifier, "]"
        print(msg1)
        print(msg2)

class story10:
    def show(self):
        msg1 = "A skeleton [HP: 10] stands before you. I am the master of endurance. It speaks. Kneel at my feet. Ready?"
        

class story11:
    def show(self):
        msg1 = "You drag yourself from the fight, your legs ache and you may have broken a bone or two. But you continue onward."
        msg2 = "[DF: ", Game.modifier, "]"
        print(msg1)
        print(msg2)

class story12:
    def show(self):
        msg1 = "A wizard [HP: 10] stands before you. I guard the life force of Magic. It whispers. None shall pass. Ready?"
        

class story13:
    def show(self):
        msg1 = "YOu drag yourself from the battle, wanting to quit. But you are so close. Onward."
        msg2 = "[MG: ", Game.modifier, "]"
        print(msg1)
        print(msg2)

class story14:
    def show(self):
        msg1 = "Finally, you staned at the base of Jade Mountain, You can see the glow of the emerald just out of reach. And then suddenly BAM a large chimera [ HP: 15] lands before you. I AM THE GUARDIAN OF THE OMNIPOTENT EMERALD. DIE MORTAL. Ready?"
        print(msg1)

class story15:
    def show(self):
        msg1 = "The beast lays slain at your feet. You reach out and toucht the emerald. You feel a great peace overtake you. All is done. Congratulations!"
        msg2 = "Final Stats: [AT: ", Game.attack, " | DF: ", Game.defense, " | MG: ", Game.magic, "]"
        print(msg1)
        print("")
        print(msg2)

class death:
    def show(self):
        msg1 = "It seems you have died great warrior. Too bad. GAME OVER"
        print(msg1)

