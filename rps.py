introduction = "Let's play Rock! Paper! Scissors!"
print(introduction)
name1 = input("Please provide player one's name: ")
name2= input("Please provide player two's name: ")

AnotherGame = "Y"
while(AnotherGame == "Y"):
  choice1= input(name1 + ": Please select your item. Type one of the following: Rock, Paper, or Scissors: ")
  choice2=input(name2 + ": Please select your item. Type one of the following: Rock, Paper, or Scissors: ")

  print("Rock! Paper! Scissors! Shoot!")

  if choice1 == choice2:
    print("Draw! Duel again!")
  elif (choice1 == "Rock" and choice2 == "Paper"):
    print("Paper covers Rock. " + name2 + " wins! Congratulations!")
  elif (choice1 == "Paper" and choice2 == 'Scissors'):
    print("Scissors cut Paper. " + name2 + " wins! Congratulations!")
  elif (choice1 == "Scissors" and choice2 == 'Rock'):
    print("Rock crushes Scissors. " + name2 + " wins! Congratulations!")
  elif (choice1 == "Rock" and choice2 == 'Scissors'):
    print("Rock crushes Scissors. " + name1 + " wins! Congratulations!")
  elif (choice1 == "Paper" and choice2 == 'Rock'):
    print("Paper covers Rock. " + name1 + " wins! Congratulations!")
  elif (choice1 == "Scissors" and choice2 == 'Paper'):
    print("Scissors cut Paper. " + name1 + " wins! Congratulations!")
  
  AnotherGame = input("Do both players want to play again? Y or N? ")
  if (AnotherGame == "Y"):
    print("Starting new game! ")
  elif (AnotherGame == "N"):
    print("Goodbye " + name1 + " and " + name2 + "!")
