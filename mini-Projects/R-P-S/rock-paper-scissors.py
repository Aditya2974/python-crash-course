import random 

def play():
    user = input("'r' - Rock , 'p' - paper , 's' - Scissor ")

    computer = random.choice(['r','p','s'])

    if user == computer:
        print("It's a tie")    

    # r > s , s > p , p > r
    PrintChoices(user,computer)

    is_win(user,computer)


def is_win(user,computer):

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print("You win!")
    else:
        print("You lose")


def PrintChoices(user,computer):
    print("Your choice is : ",user)

    print("The computer's choice is : ", computer)


play()