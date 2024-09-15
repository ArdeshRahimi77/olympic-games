import random
print("Welcome to the olympic games!")

name1 = input("Player1, what is your name?")
name2 = input("Player2, what is your name?")
name3 = input("Player3, what is your name?")

country1 = input(f"{name1}, where are you from?")
country2 = input(f"{name2}, where are you from?")
country3 = input(f"{name3}, where are you from?")

randomNumber1 = random.randint(0,3)
randomNumber2 = random.randint(0,3)
randomNumber3 = random.randint(0,3)
computerMove1 = "Gold"
computerMove2 = "Silver"
computerMove3 = "Bronze"

if randomNumber1 == 0:
    computerMove1 = "Gold"
elif randomNumber1 == 1:
    computerMove1 = "Silver"
elif randomNumber1 == 2:
    computerMove1 = "Bronze"

if randomNumber2 == 0:
    computerMove2 = "Gold"
elif randomNumber2 == 1:
    computerMove2 = "Silver"
elif randomNumber2 == 2:
    computerMove2 = "Bronze"
    
if randomNumber3 == 0:
    computerMove3 = "Gold"
elif randomNumber3 == 1:
    computerMove3 = "Silver"
elif randomNumber3 == 2:
    computerMove3 = "Bronze"

player1 = input(f"{name1} from {country1}, your place is: {computerMove1} ")
player2 = input(f"{name2} from {country2}, your place is: {computerMove2}")
player3 = input(f"{name3} from {country3}, your place is: {computerMove3}")