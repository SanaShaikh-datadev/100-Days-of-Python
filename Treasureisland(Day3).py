print("Welcome to Treasure island.\n Your mission is to find treasure\n")
press=input("You're at a cross road. Where do you want to go? Type" '"left"' 'or' '"right"\n').lower()
if(press=='right'):
    print("You fell into a hole.Game over")
elif(press=='left'):
    press2=input("You've come to a lake. There is an island in the middle of the lake. Type "'"wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if(press2=='wait'):
        press3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if(press3=='blue'):
            print("You enter a room of beasts. Game Over.")
        elif(press3=='red'):
            print("It's a room full of fire. Game Over")
        elif(press3=='yellow'):
            print("Hurrayyy!!! You find the tresure")
        else:
            print("Please select right option..start again!!")
    elif(press2=='swim'):
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Please select right option..start again!!")
else:
    print("Please select right option..start again!!")