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

choice1 = input("You have come to a cross roads, do you go left or right?")
choice1 = choice1.lower()

if choice1 == "left":
    print("Good choice! ")
    choice2 = input("You have now arrive at a lake. Do you want to swim across or wait for a boat?")
    choice2 = choice2.lower()
    if choice2 == "wait":
        print("Waiting for a boat was the correct choice.")
        choice3 = input("You now see 3 doors, one red, one yellow, one blue. What door do you choose?")
        choice3 = choice3.lower()
        if choice3 == "yellow":
            print("Great job! You Win!!")
        elif choice3 == "blue":
            print("You were eated by beasts. Game over")
        elif choice3 == "red":
            print("You were burned by fire. Game over.")
        else:
            print("Game over.")
    else:
        print("The water was too cold, you drowned. Game Over")
else:
    print("Sorry, you were eaten by a sabertooth tiger. Game over")
    






