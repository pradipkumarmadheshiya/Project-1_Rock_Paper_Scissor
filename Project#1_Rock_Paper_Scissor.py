from random import randint
cChoice={1:"⛰️",2:"📃",3:"✂️"}
while True:
    print("Rock Paper Scissor Game:-")
    yourPoints,computerPoints=0,0
    for i in range(1,6):
        print()
        print("Round",i,"start:")
        print()
        print("Please select any one option-")
        print(str(1)+" for ⛰️",str(2)+" for 📃",str(3)+" for ✂️",sep="\n")
        print()

        yourChoice=int(input())
        if yourChoice==1:
            print("You selected: ⛰️")
        elif yourChoice==2:
            print("You selected: 📃")
        elif yourChoice==3:
            print("You selected: ✂️")
        else:
            print("Invalid selection")
            break

        computerChoice=cChoice[randint(0,2)]
        
        if computerChoice==cChoice[yourChoice]:
            print("Computer selected:",computerChoice)
            print("Tie")
            print("Computer points:",computerPoints)
            print("Your points:",yourPoints)

        elif (yourChoice==1 and computerChoice==cChoice[3]) or (yourChoice==2 and computerChoice==cChoice[1]) or (yourChoice==3 and computerChoice==cChoice[2]):
            yourPoints+=1
            print("Computer selectd:",computerChoice)
            print("You wins")
            print("Your points:",yourPoints)
            print("Computer points:",computerPoints)
        else:
            computerPoints+=1
            print("Computer selected:",computerChoice)
            print("Computer wins")
            print("Computer points:",computerPoints)
            print("Your points:",yourPoints)
        print()

    if yourPoints>computerPoints:
        print("👏You wins this match")
    elif yourPoints<computerPoints:
        print("😔You lose this match")
    else:
        print("Match drawn")
    print()
    print("If you want to continue the game, Press yes")
    print("else: Press no")
    yourNeed=input()
    if yourNeed=="yes" or yourNeed=="YES" or yourNeed=="Yes":
        continue
    else:
        break