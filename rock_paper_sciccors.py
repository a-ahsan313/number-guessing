import random

def check(user, computer):
    if user == computer:
        return 0
    elif user == 0 and computer == 1:
        return -1
    elif user == 1 and computer == 2:
        return -1
    elif user == 2 and computer == 0:
        return -1

user_won = 0
computer_won = 0

dic = {0 : "Rock", 1 : "Paper", 2 : "Sciccors"}
while True:
    computer = random.randint(0, 2)
    user = int(input("Enter one Number(\'0\' for Rock, \'1\' for Paper \'2\' for Sciccors & \'9\' for Quit): "))
    if user == 9:
        break

    if user > 2 or user < 0:
        print("Please Enter the Number from (0 to 2)!")
        quit()
    else:
        checkwinner = check(user, computer)
        print(f"You Choose {dic[user]}")
        print(f"The Computer Choose {dic[computer]}")
        if checkwinner == 0:
            print("The Match is Draw!")
        elif checkwinner == -1:
            print("You Lose!")
            computer_won += 1
        else:
            print("You Won!")
            user_won += 1

print(f"You Won {user_won} times.")
print(f"The Computer Won {computer_won} times.")
print("Good Bye!")
