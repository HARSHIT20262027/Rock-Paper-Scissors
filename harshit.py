while  True:


    import  random

    choice = ["rock","paper ","scissors"]

    name = input("enter your name :- ")
    user = input("enter your choice  \n rock \n paper \n scissors  \n :- ")

    computer =  random.choice(choice)

    print("computer choice =" , computer)
    
    if user ==  computer:
            print("draw")

    elif (user ==  "rock"  and computer == "scissors") or \
        (user ==  "scissors" and computer == "paper") or \
        (user ==  "paper"  and computer == "rock "):
        print(f"congratulation  you won you choice is {user} and  cumputer choice is {computer} ")
        break

    else:
         print("oops soory computer won ")
         

    
    
