import random

lst=["rock","paper","scissor"]

def input_checker():
    while True:
        print("Type 'r' for rock,'p' for paper,'s' for scissor..")
        user_choice=input("Enter Your Choice (rock,paper,scissor):")
        if user_choice=="r":
            return lst[0]
        if user_choice=="p":
            return lst[1]
        if user_choice=="s":
            return lst[2]
        print("Invalid input..Type again")

if __name__=="__main__":
    print("===========================================================")
    print("\t      Rock Paper Scissor Game")
    print("===========================================================")
    print("GAME RULES:")
    print("""\tRock Vs Paper->Paper Wins,
        Rock Vs Scissor->Rock Wins,
        Paper Vs Scissor->Scissor""")
    user=input("Enter Your name:")
    print("Welcome "+user)
    print("Lets play..")
    while True:
        user_choice=input_checker()
        comp_choice = random.choice(lst)
        comp_choice.lower()

        print("Your Choice:" + user_choice)
        print("Computer's Choice:" + comp_choice)
        if (comp_choice == user_choice):
            print("It is a Die")
        elif ((comp_choice == "paper") and (user_choice == "rock")):
            print("Rock Vs Paper->paper Wins")
            print("*** Computer Wins ***")
        elif ((comp_choice == "rock") and (user_choice == "paper")):
            print("rock Vs Paper->Paper Wins")
            print("***" + " " + user + " " + "Wins ***")
        elif ((comp_choice == "rock") and (user_choice == "scissor")):
            print("rock Vs Scissor->rock Wins")
            print("*** Computer Wins ***")
        elif ((comp_choice == "scissor") and (user_choice == "rock")):
            print("rock Vs Scissor->Stone Wins")
            print("***" + " " + user + " " + "Wins ***")
        elif ((comp_choice == "scissor") and (user_choice == "paper")):
            print("Paper Vs Scissor->Scissor Wins")
            print("*** Computer Wins ***")
        elif ((comp_choice == "paper") and (user_choice == "scissor")):
            print("Paper Vs Scissor->Scissor Wins")
            print("***" + " " + user + " " + "Wins ***")
        choice = input("Press 1 to play again...0 for Exit")
        if choice=='1':
            continue
        else:
            print("Thanks For playing.....")
            break
    
    
    
 
