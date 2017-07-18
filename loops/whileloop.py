# for i in range(10):
#     print("i is now {}".format(i))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1
else:  # acts the same as 'for' loop
    # executes if while terminates when it's exit condition is false
    print("Finished counting")

available_exits = ["east", "north east", "south"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over!")
        break
else:
    print("Congratz, you're free")

# Guess game
import random

highest = 10
answer = random.randint(1, highest)  # [1, 10]

print("Please guess a number between 1 and {}".format(highest))
guess = -1

while guess != answer:
    guess = int(input("Your guess: "))
    if (guess > answer):
        print("guess lower")
    elif (guess < answer):
        print("guess higher")
else:
    print("Congratulations, You won! The answer was {}.".format(answer))
