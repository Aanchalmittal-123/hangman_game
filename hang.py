import random
def k():
    word=random.choice(["pugger","aanchal","himanshu","sulabh","mittal","walia","kaur","simran","amanat","bir"])
    v_list="abcdefghijklmnopqrstuvwxyz"
    turn=10
    guess_made=''
    while len(word)>0:
        main=""
        miss=0
        for l in word:
            if l in guess_made:
                main=main+l
            else:
                main=main+"_"+""
        if main==word:
            print(main)
            print("YEH YOU WON")
            break
        print("guess the word",main)
        guess=input()
        if guess in v_list:
            guess_made+=guess
        else:
            print("ENTER THE VALID CHARACTER")
            guess=input()
        if guess not in word:
            turn=turn-1
            if turn==9:
                print("9 chances left")
                print("-----------")
            if turn==8:
                print("8 chances left")
                print("-----------")
                print("     0     ")
            if turn==7:
                print("7 chances left")
                print("-----------")
                print("     0     ")
                print("     |     ")
            if turn==6:
                print("6 chances left")
                print("-----------")
                print("     0     ")
                print("     |     ")
                print("    /      ")
            if turn==5:
                print("5 chances left")
                print("-----------")
                print("     0     ")
                print("     |     ")
                print("    / \    ")
            if turn==4:
                print("4 chances left")
                print("-----------")
                print("     0     ")
                print("    /|     ")
                print("    / \    ")
            if turn==3:
                print("3 chances left")
                print("-----------")
                print("     0     ")
                print("    /|\    ")
                print("    / \    ")
            if turn==2:
                print("2 chances left")
                print("-----------")
                print("     0 |   ")
                print("    /|\    ")
                print("    / \    ")
            if turn==1:
                print("1 chance left")
                print("-----------")
                print("     0 _|  ")
                print("    /|\    ")
                print("    / \    ")
                print("YOU LED THE PERSON DIE")
                print(word)
                break

name=input("ENTER YOUR NAME")
print("{} welcome".format(name))
print("######################")
print("PLEASE ENTER THE WORD OF YOUR CHOICE AND WIN!!!!!!")
k()
print()
            
        
    
