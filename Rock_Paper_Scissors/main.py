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
         