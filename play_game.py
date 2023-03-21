# Break down a bigger problem on small parts
#make a to do list, start with the easiest
#turn the problem into comments
#write code / run the code / fix the code if needed

#The game will display two instagram accounts and your goal is to guess which account has more followers.
#The game should continue until the player guess wrong, for each right guess the player win 1 point
#The instagram winner will be compared to the next one and so on.
#When the game is over display the player final score.


from game_data import data 
import random
import art

#create a function that accepts number as parameter and return an instagram account
def select_account():
    """A function to randomly pic the accounts to play the game"""

    total_accounts = len(data)    
    choosen_account = random.randint(0, total_accounts-1)    

    return data[choosen_account]


#The rounds display the information from 2 instagram accounts "name, description and country", "A and B", and ask the user to guess who has more followers. 
#create  function to Display the options, and ask the player for his guess.
def display_options(account_a, account_b):
    """Function to display the options and return the player guess"""
    

    option1 = f"Compare A: {account_a['name']}, {account_a['description']}, {account_a['country']}"
    option2 =  f"Against B: {account_b['name']}, {account_b['description']}, {account_b['country']}"
    print(art.logo)
    print(option1)
    print(art.vs)
    print(option2)      
   


#find the account with higly number of followers.
def correct_answer(account_a, account_b):
    """Return the letter that holds the account with the higly score."""

    a_followers_number = account_a['follower_count']
    b_followers_number = account_b['follower_count']
    answer = ""

    if a_followers_number > b_followers_number:
        answer = "a"
        return answer
    else:
        answer = "b" 
        return answer



# create a function call play_game
# compair the player guess with the answer and update the score:
def play_game():
    score = 0
    play = True

    account_a = select_account()
    account_b = select_account()
    while account_a == account_b:
        account_b = select_account()

    while play:
        display_options(account_a, account_b)
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        answer = correct_answer(account_a, account_b)

        if guess == answer:
            score += 1
            print(f"You are right! Current score: {score}")
            if answer == "b":
                account_a = account_b 
            account_b = select_account()
        else:
            print(f"Sorry, that is wrong. Final score: {score}")  
            play = False  

  
play_game()