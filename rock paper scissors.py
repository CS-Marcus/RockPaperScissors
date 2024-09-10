#imports the random libary 
import random 
#imports the keyboard libary 
import keyboard


'''
Gets a string from the user forcing them to input scirssors,
paper, or scissors to make sure they follow the rules of the game
'''
def get_string(prompt):
    while True:
        choice = input(prompt)

        if choice.lower().replace(" ","") == "scissors":
            return choice
        
        elif choice.lower().replace(" ","") == "paper":
            return choice
        
        elif choice.lower().replace(" ","") == "rock":
            return choice 


'''
This function creates the move that the computer does
by getting a random int from 1 - 3 and is then assigned 
rock, scissors, or paper
'''

def computer_move():
    comp_answer = random.randint(1, 3)
    
    if comp_answer == 1:
        computer_choice = "scissors"
        return computer_choice
    
    elif comp_answer == 2:
        computer_choice = "rock"
        return computer_choice

    else:
        computer_choice = "paper"
        return computer_choice
    

'''
This function determines the winner of rock paper scissors 
between the user and the computer
'''
def winner(comp, user):

    
    if comp == "rock" and user == "scissors":
        print(f"\nYour choice was {user}\n")
        print(f"The computer choice was {comp}\n")
        print("The computer has won\n")
    
    elif comp == "scissors" and user == "paper":
        print(f"\nYour choice was {user}\n")
        print(f"The computer choice was {comp}\n")
        print("The computer has won\n")

    elif comp == "paper" and user == "rock":
        print(f"\nYour choice was {user}\n")
        print(f"The computer choice was {comp}\n")
        print("The computer has won\n")

    elif user == "rock" and comp == "scissors":
        print(f"\nYour choice was {user}\n")
        print(f"The computer choice was {comp}\n")
        print("The user has won\n")

    elif user == "scissors" and comp == "paper":
        print(f"\nYour choice was {user}\n")
        print(f"The computer choice was {comp}\n")
        print("The user has won\n")

    elif user == "paper" and comp == "rock":
        print(f"\nYour choice was {user}\n")
        print(f"The computer choice was {comp}\n")
        print("The user has won\n")
    
    else:
        print(f"\nYour choice was {user}\n")
        print(f"The computer choice was {comp}\n")
        print("Tie\n")


'''
This function gets the user's choice of rock, paper, or scissors
'''
def user_move():
    user_choice = get_string("What is your choice: ")
    return user_choice


def main():
    print("\nWelcome to Rock Paper Scissors!\n")
    print("If you would like the end the program press delete, if you would like to continue press insert\n")
    
    while True:
        
        

        if keyboard.is_pressed('delete'):
            print("Program is shutting down\n")
            break

        if keyboard.is_pressed('insert'):
            winner(computer_move(), user_move())
            print("If you would like the end the program press delete, if you would like to continue press insert\n")
        

main()