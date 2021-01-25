from random import randint
 
 
def mainMenu():
    #intro and menu
    print("Welcom to Rock, Paper Scissors!\n")
    print("MENU")
    print("(1) See Rules")
    print("(2) Single Player")
    print("(3) Two Player")
    print("(4) Exit\n")
 
    #choosing which menu option
    choice = input("")
     
    if choice == "1":
        print(rules())
    elif choice == "2":
        singlePlayer()
    elif choice == "3":
        twoPlayer()
    elif choice == "4":
        endProgram()
           #rules module    
def rules():
    print("RULES")
    print("Paper Covers Rock, Rock Smashes Scissors, Scissors Cuts Paper\n")
     
    mainMenu()
 
def weaponMenu():
    print("Choose your weapon!")
    print("(1) Rock")
    print("(2) Paper")
    print("(3) Scissors")
    print("(4) Main Menu")
 
  def singlePlayer():
 
    #create a list of play options
    moves = ["rock", "paper", "scissors"]
  
    #assign a random play to the computer
    computer = moves[randint(0,2)]
  
    #set player to False
    player = False
 
    while player == False:
    #set player to True
        player = input("Choose rock, paper, or scissors! ")
        if player == computer:
                print("Tie!")
                print(score)
                 
        elif player == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", player)
                computerScore = computerScore + 1
                print(score)
                return computerScore
            else:
                print("You win!", player, "smashes", computer)
        elif player == "paper":
            if computer == "scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "scissors":
            if computer == "rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")   

            def twoPlayer():
    print("Choose Rock Paper or Scissors, try to hide your choice!\n")
    player1 = input("Player 1 : ")
    player2 = input("Player 2 : ")
    print("")
     
 
    if (player1 == 'rock' and player2 == 'scissors'):
        print ("Player 1 wins.")
 
    elif (player1 == 'rock' and player2 == 'rock'):
        print ("Tie")
 
    elif (player1 == 'scissors' and player2 == 'paper'):
        print ("Player 1 wins.")
 
    elif (player2 == 'scissors' and player2 == 'scissors'):
        print ("Tie")
 
    elif (player1 == 'paper' and player2 == 'paper'):
        print ("Tie")
 
    elif (player1 == 'paper' and player2 == 'scissors'):
        print ("Player 2 wins.")
 
    elif (player1 == 'rock'and player2 == 'paper'):
        print ("Player 2 wins.")
 
    elif (player1 == 'paper' and player2 == 'rock'):
        print ("Player 1 wins.")
 
    elif (player1 == 'scissors' and player2 == 'rock'):
        print ("Player 2 wins.")
 
 def endGame():
     
    end = input("Would you like to end the game? (yes or no) ")
    if end == "no":
        mainMenu()
    else:
        quit()
 
mainMenu()
     
         