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

game_image = [rock , paper, scissors]

while True:

    user_choice = int(input("what do you choose? type 0 for rock , 1 for paper , 2 for scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("Exiting program, invalid choice!")
        break;
    else:
        print(game_image[user_choice])
    
    computer_choice = random.randint(0,2)
    print("computer choice:")
    print(game_image[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        print("you win!")
    elif computer_choice == 0 and user_choice ==2:
        print("You lose!")
    elif computer_choice > user_choice :
        print("you lose!")
    elif user_choice > computer_choice:
        print("you win")
    elif computer_choice == user_choice:
        print("Its a Draw")









#print(rock)
#print(scissors)
#print(paper)
