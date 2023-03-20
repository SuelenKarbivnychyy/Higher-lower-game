# Break down a bigger problem on small parts
#make a to do list, start with the easiest
#turn the problem into comments
#write code / run the code / fix the code if needed

#The game will display two instagram accounts and your goal is to guess which account has more followers.
#The game should continue until the player guess wrong, for each right guess the player win 1 point
#The first instagram winner will be compared to the next one and so on.
#When the game is over display the player final score.


from game_data import data 
import random

#create a function that accepts number as parameter and return an instagram account
def select_account(number):
    """A function to randomly pic the accounts to play the game"""

    total_accounts = len(data)
    
    while number != 0:
        choosen_account = random.randint(0, total_accounts-1)
        
        account_holder_name = data[choosen_account]["name"]
        account_description = data[choosen_account]["description"]
        holder_country = data[choosen_account]["country"]
        number_followers = data[choosen_account]["follower_count"]
        account_information = [account_holder_name, account_description, holder_country, number_followers]
        number -= 1
    return account_information


#The rounds display the information from 2 instagram accounts "name, description and country", "A and B", and ask the user to guess who has more followers. 
#create  function to Display the options, and ask the player for his guess.
def display_options():
    """Function to display the options and return the player guess"""

    account_a = select_account(1)
    account_b = select_account(1)

    option1 = f"Compare A: {account_a[0]}, {account_a[1]}, {account_a[2]}, {account_a[-1]}"
    option2 =  f"Compare B: {account_b[0]}, {account_b[1]}, {account_b[2]}, {account_b[-1]}"
    print(option1)
    print(option2)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()    
    return guess


#find the account with higly number of followers.
def correct_answer(account_a, account_b):
    """Return the letter that holds the account with the higly score."""

    a_followers_number = account_a[-1]
    b_followers_number = account_b[-1]
    answer = ""

    if a_followers_number > b_followers_number:
        answer = "a"
        return answer
    else:
        answer = "b" 
        return answer



# create a function call play_game
# compair the player guess with the answer and update the score:
def play_game(guess, final_answer):
    score = 0
    play = True
     
    while True:        
        if guess == final_answer:
            score += 1
            print(f"You are right! Current score: {score}")
            # final_answer = guess
            # account_b = select_account(1) 
            break            
        else:
            print(f"Sorry, that is wrong. Final score: {score}")
            play = False
            break


final_answer = correct_answer(account_a = select_account(1), account_b = select_account(1) )

  
play_game(display_options(), final_answer)




# figuriout this function

# def play_game(guess, final_answer):
#     score = 0
    
#     while guess == final_answer:
    
#         score += 1
#         print(f"You are right! Current score: {score}")
#         print(f"THIS SHOULD BE THE SCORE {score}")

#         display_options()
#         # final_answer = guess
#         # account_b = select_account(1) 
               
#         break
    
#     print(f"Sorry, that is wrong. Final score: {score}")
    
    
# play_game(display_options(), final_answer) 



#if the users guess right the instagram account winner become A at the next round, and so on.














#just testing to return a list
# def return_options():

#     account_a = select_account(1)
#     account_b = select_account(1)

#     option1 = f"Compare A: {account_a[0]}, {account_a[1]}, {account_a[2]}"
#     option2 =  f"Compare B: {account_b[0]}, {account_b[1]}, {account_b[2]}"
    
#     options = [option1, option2]
#     return options
# print(return_options)


# def display_options(accounts):
#     """Function to display the options and return the player guess"""

#     for account in accounts:
#         print(account)
    
# print(return_options())


  