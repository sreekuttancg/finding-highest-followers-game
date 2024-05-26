import random

from art import logo,vs



from game_data import data
def random_people():
    return random.choice(data)

def random_people_details(account):
    name=account["name"]
    description=account['description']
    country=account['country']
    return f"{name}, {description}, from {country}"

def check_answer(guess,a_follower,b_follower):
    if a_follower>b_follower:
        return guess=="a"
    else:
        return  guess=="b"

def game():
    print(logo)
    score=0
    game_continue=True
    a_account=random_people()
    b_account=random_people()
    while game_continue:
        a_account=b_account
        b_account=random_people()
        # while a_account==b_account:
        #     b_account=random_people()
        print(f"Compare A:{random_people_details(a_account)}")
        print(vs)
        print(f"Against B:{random_people_details(b_account)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers_count=a_account["follower_count"]
        b_followrs_count=b_account["follower_count"]
        correct=check_answer(guess,a_followers_count,b_followrs_count)
        if correct :
            score+=1
            print(f"You're right! Current score: {score}.")
        else:
            game_continue=False
            print("You loose it! Get lost bitch")



game()
