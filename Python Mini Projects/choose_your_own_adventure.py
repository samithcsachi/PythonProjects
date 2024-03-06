name = input("Type your name : ")
print("welcome", name, " to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go ? ").lower()    
if answer == "left": 
    answer = input(" You come to a river, you can walk around it or swim across? Try walk to walk around and swim to swim accross:")
    if answer == "swim":
        print("You swim across and were eaten by an alligater. ")
    elif answer =="walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:   
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)? ")
    if answer == "cross":
        answer = input("You cross the bridge and meet the stranger. Do you talk to them (yes/no) ? ")
        if answer == "yes":
            print("You talk to the stanger and they gave you gold. YOU WIN !!! ")
        elif answer == "no":
            print("You ignore teh stanger and they are offended and lose.  ")
        else: 
            print("Not a valid option. You lose. ")
    elif answer =="back":
        print("You go back and lose  ")
    else:   
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose. ")
