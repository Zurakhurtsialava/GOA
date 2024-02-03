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
    print("You are now logged in ")
  else:
    print("Information you entered is incorrect")
else:
  print("Password is incorrect")

list_of_games = ["jadraki"]
user_input = input(f"Hello! Please choose a game {list_of_games}: ")

if user_input == "jadraki":
  print("You have selected the jadraki good luck")

choices = ["I want to skip one PAWN", "I want to move rock strate ", "i want to move rock back"]

userchoice = input(f"Please choose one {choices}: ")

pcchoice = random.choice(choices)

if userchoice == "I want to skip one PAWN" and pcchoice == "i want to move rock back" or userchoice == "I want to move rock strate " and pcchoice == "I want to skip onw pawn" or userchoice == "scissors" and pcchoice == "paper":
    print("You Won!")

elif userchoice == pcchoice:
    print("tie")
else:
    print(f"PC Won! because he choosed {pcchoice}")



