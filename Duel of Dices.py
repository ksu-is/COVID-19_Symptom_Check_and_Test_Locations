#Program to play a 2 player dice game
#Hello all, I'm Ebonee. This is a game of roll the dice. Two players take turns rolling the dice 5 times. In the end the player first to 50 is the overall winner!

def menuChoice():
  print('1: Display rules')
  print('2: Start new game')
  print('3: Quit')
  choice= int(input('What would you like to do?'))
  while int(choice) < 1 or int(choice) > 3:
    print('Ivalid choice.')
    print('Please enter a number between 1 and 3:')
    choice=input()  
  return choice
  
#Displays Rules
def displayRules():
  print('The rules of the game are as follows:')
  print('Players take turns throwing two dice.')
  print("If the roll is a 'double', ex. two 2s, two 3s, etc.,")
  print("The player's score reverts to zero and their turn ends")
  print('(etc,)')
#Each player takes a turn
import random
def playerTurn(player,score):
  print('Your turn, ',player)
  anotherGo = 'Y'
  scoreThisTurn = 0
  while anotherGo == 'Y' or anotherGo == 'y':
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print('You rolled ',die1, ' and',die2)
    if die1 == die2:
      scoreThisTurn= 0
      cumulativeScore = 0
      print('Bad luck! Press any key to continue')
      anyKey= input()
      anotherGo= 'N'
    else:
      scoreThisTurn = scoreThisTurn + die1 +die2
      cumulativeScore = score + scoreThisTurn
      print('Your score this turn is ',scoreThisTurn)
      print('Your cumulative score is ',cumulativeScore)
      if cumulativeScore>= 50:
        anotherGo = 'N'
      else:
        print('Another go? (answer Y or N)')
        anotherGo = input()
  return cumulativeScore
#To play game
def playGame():
  score1 = 0
  score2 = 0
  player1 = input("Enter Player1's name: ")
  player2 = input("Enter Player2's name: ")
  while score1 <50 and score2 <50:
    score1 = playerTurn(player1,score1)
    if score1 >=50:
      print('You are the winner!')
    else:
      score2 = playerTurn(player2,score2)
      if score2 >= 50:
        print('You are the winner!')
#main program starts
option = menuChoice()
print(option)
while option != 3:
  if option == 1:
    displayRules()
    print()
  else:
    playGame()
    menuChoice()
  option = menuChoice()
print('Goodbye!')
