import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock,paper,scissors]
handsName = ["rock","paper","scissors"]

randNum = random.randint(0,2)

print("What do you want to choose?\n")
value = int(input("1 for rock, 2 for paper, 3 for scissor: ")) - 1
print(f"You chose: {handsName[value]} {hands[value]} \n")
print(f"Computer chose: {handsName[randNum]} {hands[randNum]}\n")

if handsName[value] == handsName[randNum]:
    print("No Winner!")
else:
    if handsName[value] == "rock" and handsName[randNum] == "scissors":
        print("You have won")
    elif handsName[value] == "rock" and handsName[randNum] == "paper":
        print("You have lost!")
    elif handsName[value] == "paper" and handsName[randNum] == "rock":
        print("You have won!")
    elif handsName[value] == "paper" and handsName[randNum] == "scissors":
        print("You have lost!")
    elif handsName[value] == "scissors" and handsName[randNum] == "rock":
        print("You have lost!")
    elif handsName[value] == "scissors" and handsName[randNum] == "paper":
        print("You have won!")