# -*- coding: utf-8 -*-
# @Author: zero_kelvin
# @Date:   2021-07-02 18:50:57
# @Last Modified by:   zero_kelvin
# @Last Modified time: 2021-07-04 13:52:15

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#***********************************************************************************
#                   ===============  Game Variables  ===============                    
#***********************************************************************************
left_right = input("You have reached a cross roads. Do you want to turn left, or do you want to turn\nright? Type 'left' or 'right': \n").lower()
loser = "\n***********************************************************************************\n                    ===============  GAME OVER  ===============                    \n***********************************************************************************\n"
winner = "\n\nYou have learned much my friend\nand have earned your TREASURE.\n\n***********************************************************************************\n===============================   CONGRATULATIONS   ===============================\n***********************************************************************************\n"
right = f"You are confronted by pirates who kidnap you, beat you and then leave you for dead\non a deserted island.\n{loser}\n"
price = "'Aye tis the treasure ye be seekin'. Dangerous paths they are ahead, you may make it\nthrough but you won't find the treasure without my help!\nTake ye straight to it I can, for an even share.'"
jungle_path = "You are confronted with 3 jungle paths that look equally as dangerous."
loser = "***********************************************************************************\n                    ===============  GAME OVER  ===============                    \n***********************************************************************************\n"
alligator_trap = "You come to a small waterway with alligators lazily laying at the surface.\n"
tiger_trap = "You arrive at what appears to be a tiger trap with several dead pirates at the\nbottom. You look around for a way to safely cross the trap as there is thick jungle\non either side."
poovey_shit = "\n***********************************************************************************\n                           Holy shitsnacks dude that was                           \n               ===============   FREAKING  AWESOME   ===============               \n***********************************************************************************\n\n"
treasure_cave = "arriving at an opening to a cave that is blocked by a large stone. Carved in the\nstone is a riddle.\n"
courage = "You see two holes, one either side of the stone large enough for an arm.\nYou and the ferryman each reach in pushing through squishy things and find a lever.\nAfter a few attempts while the ferryman holds his lever yours opens the cave revealing\nthe treasure."
d_e = "Anger and suffering are not to be feared, merely minimised, you have shown great courage\n& have learned much venturing here today, however you have not found the treasure."
your_mum = "***********************************************************************************\nInteresting fact that the universe is so immense and so large, that it could just\nfit your mum.\nTrue Story\n***********************************************************************************\n"
cheat = f"UH, UH, UH... You can't cheat your way through!\n{loser}"

#***********************************************************************************
#                   ===============  Riddle  ===============                    
#***********************************************************************************

riddle = "-----------------------------------------------------------------------------------\n'Archimedes said he could move me with his hand, yet fulcrum is his closest friend.\nIn the darkest of places we reach and find what we fear most is in our mind!'\n-----------------------------------------------------------------------------------\n"
riddle_answer_a = "world"
riddle_answer_b = "ship"
riddle_answer_c = "your mum"
riddle_answer_d = "suffering"
riddle_answer_e = "anger"
riddle_answer_f = "fear"
riddle_answers = riddle_answer_a, riddle_answer_b, riddle_answer_c, riddle_answer_d, riddle_answer_e, riddle_answer_f
correct = riddle_answer_a, riddle_answer_f

#***********************************************************************************
#                      ===============  Game  ===============                      
#***********************************************************************************

if left_right == "right":
    print(f"{right}")
if left_right == "left":
    print("\nYou arrive at a lake where two boats are tied up at a dock.\nOne boat is manned by a ferryman who offers to take you across to the other side for\na price.\n\nHowever he will not tell you the price until you get to the other side.\nThe other boat is EMPTY and is in better condition than the ferryman's boat.")
    boat = input("Which boat do you choose to cross the lake in. Type either 'accept' or 'decline':\n").lower()
    if boat == "decline":
        print(f"You take the empty boat and row until half way across the boat creaks, cracks & breaks, quickly sinking.\nThis forces you to swim the rest of the way only just making it.\nCollapsing on the beach you find a band of pirates are waiting for you.\n{loser}")
    if boat == "accept":
        print(f"\nThe boatman seems a delightful fellow who regales you with stories during the crossing\nand is a perfect host.\nUpon reaching the far side he turns to you and says.\n{price}")
        even_share = input("Accept his offer type 'accept'. Decline his offer type 'decline'. \n").lower()
        if even_share == "decline":
            print(f"\nThe ferryman nods politely and charges you two gold coins which you pay happily,\nthanking him before going on your way.\n{jungle_path}")
            direction = input("To choose a jungle path type 'right', 'centre' or 'left':\n").lower()
            if direction == "right":
                print(f"{right}")
            elif direction == "centre" or direction == "center":
                print(f"{alligator_trap}\nThrough cunning and gyle you pass the danger and leave as quickly as you can")
                print(f"{treasure_cave}{riddle}\nThe riddle has you stumped.\nAs hard as you try you are unable to move the stone.\n{loser}")
            elif direction == "left":
                print(f"{tiger_trap}")
                trap = input("There is a rope vine hanging just out of reach and you think you can jump to it and\nswing safely across.\nThere is also a fragile looking log that will reach across the pit.\nType 'log' to use the log or type 'swing' to use the rope-vine.\n").lower()
                if trap =="log":
                    print(f"You have chosen poorly. The log breaks and you fall into the trap.\nImpaled through the leg by one of the many spikes you succumb to your wounds.\n{loser}")
                if trap == "swing":
                    print("You take a running jump and catch the vine swinging across the trap and landing with\na perfect dismount.")
                    print(f"{poovey_shit}You made it across the trap.\nYou continue on and make it across many more traps and dangers and finally\n{treasure_cave}\n{riddle}\nAs hard as you try you are stumped by the riddle\n{loser}")
        if even_share == "accept":
            print("\nYou accept his offer and he guides you down the central path.")
            print(f"{alligator_trap}The ferryman suggests running across the alligators backs. You reluctantly agree\nand choose a path each.\nYou then make the dash across the backs of the alligators and barely make it across.\n{poovey_shit}You continue on through the jungle.\n")
            print(f"{treasure_cave}{riddle}\nThe ferryman knows his stuff and gives you the clue you need...\n")
            answer1 = input("What did Archimedes say he could move?\nType 'world', a 'ship' or 'your mum':\n").lower()
            answer2 = input("What should we fear most... If fear leads to anger, anger leads to hate, hate leads\nto suffering.?\nType suffering, anger or fear:\n").lower()
            if answer1 == str(riddle_answer_a) and answer2 == str(riddle_answer_f):
                print(f"{courage}\n{winner}")
            if answer1 == "your mum":
                print(f"{your_mum}\n{loser}")
            elif answer1 != str(riddle_answer_a) or answer2 != str(riddle_answer_f):
                print(f"Sorry my friend, better luck next time.\n{d_e}\n{loser}")

