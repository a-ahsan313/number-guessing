# Quiz Game by using Python

print("Welcome to the Quiz Game!!")

playing = input("Do you want the Quiz Game? ")
if playing.lower() != "yes":
    quit()

print("Okay, Lets Play the Game..:) ")

score = 0

answer1 = input("What does CPU stands for? ")
if answer1.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("What does GPU stands for? ")
if answer2.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("What does RAM stands for? ")
if answer3.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("What does ROM stands for? ")
if answer4.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {str(score)} questions correct.")
print(f"You got {str((score/4) * 100)} %")