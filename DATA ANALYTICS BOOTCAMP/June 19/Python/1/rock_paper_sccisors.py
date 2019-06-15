import random
print ("Lets Play Rock, Paper, Scissors!")
options = ["r","p","s"]
options_full = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)
if computer_choice == "r":
    computer_choice = "Rock"
elif computer_choice == "p":
    computer_choice = "Paper"
elif computer_choice == "s":
    computer_choice = "Scissors"
user_choice = input("Choose your weapon: (r)ock, (p)aper, (s)cissors: ")
if user_choice == "r":
    user_choice = "Rock"
elif user_choice == "p":
    user_choice = "Paper"
elif user_choice == "s":
    user_choice = "Scissors"

if (user_choice == options_full[0] and computer_choice == options_full[2]) or (user_choice == options_full[1] and computer_choice == options_full[0]) or (user_choice == options_full[2] and computer_choice == options_full[1]):
    print(f"\nYou choose {user_choice} and your enemy choose {computer_choice}, you won!")
elif (user_choice == options_full[0] and computer_choice == options_full[0] or (user_choice == options_full[1] and computer_choice == options_full[1]) or (user_choice == options_full[2] and computer_choice == options_full[2])):
    print(f"\nYou choose {user_choice} and your enemy choose {computer_choice}, it's a tie!")
else:
    print(f"\nYou choose {user_choice} and your enemy choose {computer_choice}, you lose!")
    
    
    
    



    


