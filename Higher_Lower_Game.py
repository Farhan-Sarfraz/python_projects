import random
import os

data = [
   {"name" : "Cristiano Ronaldo", "followers" : 500, "country" : "portugal", "profession" : "footballer"},
   {"name" : "mMssi", "followers" : 300, "country" : "argentina", "profession" : "footballer"},
   {"name" : "Neymar", "followers" : 120, "country" : "brazil", "profession" : "footballer"},
   {"name" : "Shakira", "followers" : 400, "country" : "american", "profession" : "singer"},
   {"name" : "Kohli", "followers" : 340, "country" : "india", "profession" : "cricketer"},
   {"name" : "The Rock", "followers" : 430, "country" : "american", "profession" : "actor, wwe superstar"},
   {"name" : "Muhammad ali", "followers" : 90, "country" : "american", "profession" : "boxer"},
   {"name" : "Imran khan", "followers" : 45, "country" : "pakistan", "profession" : "politician, cricketer"},
]

def formate_data(account):
    """ Takes the account data and print the return statements. """
    account_name = account["name"]
    account_profession = account["profession"]
    account_country = account["country"]

    return f"{account_name}, a {account_profession}, from {account_country}"

def checking_answer(guess, account_follower_a, account_follower_b):
    """ Takes the user guess and account followers and return the highest.. """
    if account_follower_a > account_follower_b:
        return guess == "a"
    else:
        return guess  == "b"
    
score = 0

game_should_continue = True
b_account = random.choice(data)
while game_should_continue:
    a_account = b_account
    b_account = random.choice(data)

    while  a_account == b_account:
        b_account= random.choice(data)  

    print(f"compare A: {formate_data(a_account)}")

    print(" VS ")

    print(f"Against B: {formate_data(b_account)}")

    guess = input("Who has more followers ? type 'a' or 'b' : ").lower()


    account_follower_a = a_account["followers"]
    account_follower_b = b_account["followers"]
    is_correct = checking_answer(guess, account_follower_a, account_follower_b)


    if is_correct:
        score += 1
        print(f"You'r right! final score is {score}")
    else:
        game_should_continue = False
        print(f"You'r wrong! final score is {score}")

