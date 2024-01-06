import random
print("           "" ROCK PAPER SCISSORS ""            ")
print("           "" Welcome to the game ""            ")
print("|-------------------------------------------|")
print("|   RULES                                   |")
print("|   Rock vs Paper -> Paper wins             |")
print("|   Rock vs Scissors -> Rock wins           |")
print("|   Scissors vs Paper -> Scissor wins       |")
print("|-------------------------------------------|")
while(True):
    print("Rock Paper Scissor?? \n 1.Rock \n 2.Paper \n 3.Scissor")
    ch=int(input("Enter your choice: "))
    while ch > 3 or ch < 1:
        ch=int(input("Enter a valid choice please: "))

    if ch == 1:
        ch_name="Rock"
    elif ch == 2:
        ch_name="Paper"
    else:
        ch_name="Scissors"

    print("User choice is \n",ch_name)
    print("Computers Turn .....")

    comp_ch=random.randint(1,3)
    if comp_ch == 1:
        comp_ch_name="ROCK"
    elif comp_ch == 2:
        comp_ch_name="PAPPER"
    else:
        comp_ch_name="SCISSOR"
    print("Computer choice is \n",comp_ch_name)
    print(ch_name,"vs",comp_ch_name)

    if ch==comp_ch:
        print("Draw =>",end="")
        result='Draw'

    if (ch==1 and comp_ch==2):
        print("Paper wins =>",end="")
        result='PAPPER'
    elif (ch==2 and comp_ch==1):
        print("Paper wins =>",end="")
        result='Paper'

    if (ch==1 and comp_ch==3):
        print("Rock wins =>",end="")
        result='Rock'
    elif (ch==3 and comp_ch==1):
        print("Rock wins =>",end="")
        result='ROCK'

    if (ch==2 and comp_ch==3):
        print("Scissors wins =>",end="")
        result='SCISSOR'
    elif (ch==3 and comp_ch==2):
        print("Scissors wins =>",end="")
        result='Scissor'

    if result == "Draw":
        print("Its a tie \n")
    if result == ch_name:
        print(" You win \n")
    if result == comp_ch_name:
        print("Computer wins  \n")

    a=input("Want to play again?? (y/n):")
    if a =='n':
        break

print("Thanks for playing")
    
        
    
