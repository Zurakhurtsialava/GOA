import random

   

username = input("Enter your name: ")
password = input("Enter your password ( 1 - 8+ ): ")
repeatpass = input("Repeat the password: ")

if repeatpass == password:
  print("You Succesfully registered!")
  print("You may Login")
  lusername = input("Enter your name: ")
  lpassword = input("Enter your password: ")
  if lusername == username and lpassword == password:
    print("You are now logged in")
  else:
    print("Information you entered is incorrect")
else:
  print("Password is incorrect")


list_of_games = ["dr", "rps"]

user_input = input(f"Hello! Please choose a game {list_of_games}: ")

if user_input == "rps":
  
  print("You have selected the rps good luck")

  choices = ["rock", "paper", "scissors"]

  userchoice = input(f"Please choose one {choices}: ")

  pcchoice = random.choice(choices)

  if userchoice == "rock" and pcchoice == "scissors" or userchoice == "paper" and pcchoice == "rock" or userchoice == "scissors" and pcchoice == "paper":
    print("You Won!")

  elif userchoice == pcchoice:
    print("tie")

  else:
    print(f"PC Won! because he choosed {pcchoice}")
if user_input == "dr":
  print("you have selecdet the dr good luck")
  my_list = [1,2,3,4,5,6]
  user = random.choice(my_list)
  pc = random.choice(my_list)
  if user > pc:
    print("user win",user)
  elif user == pc: 
    print("tie")
  else:
    print("pc win",pc)
  