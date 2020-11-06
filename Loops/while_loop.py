import math
import random

# WHILE LOOP
# i = 1
# while i <= 5:
#     print('* ' * i)
#     i += 1
# print("Done")

# NUMBER GUESSING GAME
# random_number = random.randrange(1, 10)
# guess_count = 0
#
# print("Try to guess the right number. You only have 3 tries!")
# while guess_count < 3:
#     guess = int(input("Guess a number: "))
#     guess_count += 1
#     if guess == random_number:
#         print("YOU GOT IT!!!")
#         break
#     elif guess_count != 3:
#         print(f"Nope... You have {3 - guess_count} tries left")
#     else:
#         print("You lose")
# print(f"The number was {random_number}")

# WHILE LOOP CAR GAME
# print("type help for list of commands")
# is_started = False
# while True:
#     user_input = input("> ").lower()
#     if user_input == "help":
#         print("Type 'start' to start the car")
#         print("Type 'stop' - to stop the car")
#         print("Type 'quit' - to exit")
#     elif user_input == "start" and is_started is False:
#         is_started = True
#         print("Car started: Vroom Vroom")
#     elif user_input == "start" and is_started is True:
#         print("The car is already started!")
#     elif user_input == "stop" and is_started is False:
#         print("Car is already stopped...")
#     elif user_input == "stop" and is_started is True:
#         is_started = False
#         print("Car stopped")
#     elif user_input == "quit":
#         break
#     else:
#         print("That is not a valid command. Type help to see a list of valid commands.")
