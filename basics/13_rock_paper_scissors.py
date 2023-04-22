import random

# Make a two-player Rock-Paper-Scissors game. 
options = [
    "rock",     # rock:scissor = rock, rock:paper = paper 
    "paper",    # paper:rock = paper, paper:scissor = scissor
    "scissors", # scissor:paper = scissor, scissor:rock = rock
]
bot = random.choice(options)
#user_input = random.choice(options)
draw = False
user_input = input("Choose Rock, Paper or Scissors: ").lower()

if user_input == bot: 
    draw = True    
elif user_input == options[0]: # user input rock
    if bot == options[1]: # bot input paper
        userwin = False 
    else:
        userwin = True
elif user_input == options[1]: # user input paper
    if bot == options[2]: # bot input paper
        userwin = False 
    else:
        userwin = True

elif user_input == options[2]: # user input scissor 
    if bot == options[0]: # bot input paper
        userwin = False 
    else:
        userwin = True
else: 
    print("Ya moms a hoe.")
    exit(1)

if draw == True:
    print("Draw!!!")
elif userwin == True:
    print("Congrats you win!")
else:
    print("L nerd u suck")

