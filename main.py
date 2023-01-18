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

randNum = random.randint(0,2)

print("What do you want to choose?\n")
value = int(input("1 for rock, 2 for paper, 3 for scissor\n")) - 1
print(f"You chose: {hands[value]} ")
print(f"Computer chose:\n")
print(hands[randNum])