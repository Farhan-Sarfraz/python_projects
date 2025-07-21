
import  random

def play_game():

    print("\n === Welcome To Number Guessing Game == \n")
    print(" I'm thinking number guessing between (1 and 100). ")

    number_input = random.randint(1, 100)
    
    while True:
        choose_dificulty = input("Choose the dificulty : type 'hard' or 'easy' : ").lower()
        if choose_dificulty == 'easy':
            attempts = 10
            print("You have 10 attempts. ")
            break
        elif choose_dificulty == 'hard':
            attempts = 5
            print("You have only 5 attempts. ")
            break
        else:
            print("Invalid choice. Please type 'easy' or 'hard' .")
    

    while attempts > 0:
        user_guess = int(input("guess the number. "))
        
        if user_guess > number_input:
            print("Too high. ")
            attempts -= 1
        elif user_guess < number_input:
            print("Too low. ")
            attempts -= 1
        else:
            print("You win. ")
            return
        
        if attempts > 0:
            print(f"Attempts remaining : {attempts} ")
        else:
            print(f"Your attempts completed now. and correct number is : , {number_input} ")

while True:
    play_game()
    play_again = input(f"Do you want to play game again : type 'y'or 'n'.").lower()
    if play_again != 'y':
        print("Thanks for playing the game. ")
        break






