import random
import time

decisions = ["r", "p", "s", "q"]
COM_Points = 0
Player_Points = 0

while True:
    winStatus = 0
    computerChoose = decisions[random.randint(0, 2)]
    print("Welcome to a game of Rock Paper Scissors...")
    print("Player {} : Computer {}".format(Player_Points, COM_Points))
    time.sleep(1)
    while True:
        print("Choose (r)ock, (p)aper, (s)cissors or (q)uit")
        playerChoose = input()

        match playerChoose:
            case "r":
                break
            case "p":
                break
            case "s":
                break
            case "q":
                break
            case _:
                print("Wrong input")

    if computerChoose == playerChoose:
        print("Draw")
        continue

    if playerChoose == "q":
        print("bye bye")
        time.sleep(1)
        break

    if computerChoose == "r":
        if playerChoose == "p":
            winStatus = 1
            print("you win")
        if playerChoose == "s":
            winStatus = -1
            print("you lose")

    if computerChoose == "p":
        if playerChoose == "r":
            winStatus = -1
            print("you lose")
        if playerChoose == "s":
            winStatus = 1
            print("you win")

    if computerChoose == "s":
        if playerChoose == "r":
            winStatus = 1
            print("you win")
        if playerChoose == "p":
            winStatus = -1
            print("you win")

    if winStatus == 1:
        Player_Points = Player_Points + 1
    if winStatus == -1:
        COM_Points = COM_Points + 1

    time.sleep(2)
