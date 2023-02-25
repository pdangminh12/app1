# PASSWORD STORING
import random

password = input("Create a password (at least 8 letters/numbers): ")

while len(password) < 8:
    print("Password is not long enough! Make sure it has at least 8 characters!")
    password = input("Create a password (at least 8 letters/numbers): ")

password_confirm = input("Confirm your password: ")

while password_confirm != password:
    print("Confirm your password again!")
    password_confirm = input("Confirm your password: ")

print(f"Success!")


def login():
    password_enter = input("Enter your password: ")
    trials = 5
    while password_enter != password and trials > 1:
        trials = trials - 1
        print(f"Incorrect password! You have {trials} trials left!")
        password_enter = input("Enter your password: ")
        if trials == 1:
            print("You're out of trials!")
            exit()
    print("Welcome!")


login()
app_choice = int(input("What app do you want to use? (1 for Calculator, 2 for Rock-Paper-Scissors) "))

# BASIC CALCULATOR


def calculator():
    def process():
        choice = int(input("What would you like to do? (1 for +; 2 for -; 3 for *; 4 for /; 5 for % (modulus); 6 for //)\n"))

        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))

        if choice == 1:
            ans = num1 + num2
            print(f"{num1} + {num2} = {ans}")

        elif choice == 2:
            ans = num1 - num2
            print(f"{num1} - {num2} = {ans}")

        elif choice == 3:
            ans = num1 * num2
            print(f"{num1} * {num2} = {ans}")

        elif choice == 4:
            ans = num1 / num2
            print(f"{num1} / {num2} = {ans}")

        elif choice == 5:
            ans = num1 % num2
            print(f"{num1} % {num2} = {ans}")

        elif choice == 6:
            ans = num1 // num2
            print(f"{num1} // {num2} = {ans}")
        else:
            print("Error!")
            exit()
    process()
    again2 = input("Use again? (Y for Yes, N for No): ")
    while again2 == "Y":
        process()
        again2 = input("Use again? (Y for Yes, N for No): ")
    print("Goodbye!")
    exit()

# ROCK-PAPER-SCISSORS


def rps_game():
    def rps():
        plr_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))
        com_choice = random.randint(1, 3)
        if (plr_choice == 1 and com_choice == 2) or (plr_choice == 2 and com_choice == 3)\
            or (plr_choice == 3 and com_choice == 1):
            print("You lost!")
        elif (plr_choice == 1 and com_choice == 3) or (plr_choice == 2 and com_choice == 1)\
            or (plr_choice == 3 and com_choice == 2):
            print("You won!")
        else:
            print("Draw!")
    rps()
    again = input("Play again? (Y for Yes, N for No): ")
    while again == "Y":
        rps()
        again = input("Play again? (Y for Yes, N for No): ")
    print("Goodbye!")
    exit()


while app_choice == 1 or app_choice == 2:
    if app_choice == 1:
        calculator()
    elif app_choice == 2:
        rps_game()
