import random

randomNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print("Guess a number?  / tries{}".format(guessTaken))
    guess = int(input())

    if guess > randomNumber:
        print("Wrong number, go a little lower")
    if guess < randomNumber:
        print("Wrong number, go a little higher")
    if guess == randomNumber:
        break

if guess == randomNumber:
    print("nice")
else:
    print("Sadly the number was {}".format(randomNumber))
