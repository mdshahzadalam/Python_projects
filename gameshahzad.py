import random
lst=['s','w','g']
chance =10
no_of_chance=0
computer_point=0
human_point=0
print("\n\n\n\n\n\nSnake Water and Gun Game\n\n")
print("\ns for Snake \n w for Water \n g for Gun\n")
while no_of_chance< chance:
    print("Please select one ......")
    _input=input("Snake Water Gun: ")
    _random=random.choice(lst)
    if _input==_random:
        print("Tie both 0 point to each \n")
    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(f"Your guess {_input} and Computer guess is {_random}\n")
        print("Computer win 1 point\n")
        print(f"Computer point is {computer_point} and Human point is {human_point}\n")
    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"Your guess {_input} and Computer guess is {_random}\n")
        print("Human win 1 point\n")
        print(f"Computer point is {computer_point} and Human point is {human_point}\n")
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and Computer guess is {_random}\n")
        print("Computer win 1 point\n")
        print(f"Computer point is {computer_point} and Human point is {human_point}\n")
    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"Your guess {_input} and Computer guess is {_random}\n")
        print("Human win 1 point\n")
        print(f"Computer point is {computer_point} and Human point is {human_point}\n")
    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"Your guess {_input} and Computer guess is {_random}\n")
        print("Human win 1 point\n")
        print(f"Computer point is {computer_point} and Human point is {human_point}\n")
    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"Your guess {_input} and Computer guess is {_random}\n")
        print("Computer win 1 point\n")
        print(f"Computer point is {computer_point} and Human point is {human_point}\n")
    else:
        print("You have input wrong\n")

    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")
print("\n\n\nGame Over\n\n\n")

if computer_point>human_point:
    print("Computer wins and You loose")
if computer_point<human_point:
    print("You wins and Computer loose")
else:
    print("Tie both 0 point to each")
print(f"Your point is {human_point} and Computer point is {computer_point}")

