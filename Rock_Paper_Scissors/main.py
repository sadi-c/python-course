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
         