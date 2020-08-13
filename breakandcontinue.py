
import random
print("Welcome to Number Guessing game developed by Arpit Patel!!!")

random_number = random.randint(1,50) # Generates random numbers between 1 to 50
count = 1 # set counter to 1

while(True):

    user_input = int(input("\n Guess any number between 1 to 50: "))

    if count == 9 and user_input == random_number:
        print(f"\n Whoo Whoo, its your day buddy!!! your guessed correctly on last attempt")
        break

    elif count == 9:
        print(f"\n game over!!!!!,{count} attempts are finish, better luck next time ")
        break

    elif user_input < random_number:
        print("Your guess was too low: Guess a number higher than", user_input)
        print(f"{9-count} attemps left")
        print("Please try again")
        count = count + 1

    elif user_input > random_number:
        print("Your guess was too high: Guess a number lower than", user_input)
        print(f"{9-count} attempts left")
        print("Please try again")
        count = count + 1

    elif user_input == random_number:
        print(f"\n Congratulations you won, you took {count} attempts.")
        break

    else:
        print("Something went wrong...")




