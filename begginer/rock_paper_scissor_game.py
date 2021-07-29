import random
while True:

    print("1 -- rock")
    print("2 -- paper")
    print("3 -- scissor")
    print("4 -- exit from game")
    a = random.randrange(1,4)
    b = input("enter your choice --> ")
    if (a==1 and b==2): 
        print("you win !!!")
    elif (a==1 and b==3):   
        print("you loose....")
    elif (a==2 and b==1):   
        print("you loose.....")
    elif (a==2 and b==3):   
        print("you win !!!!!")
    elif (a == 3 and b==1): 
        print("you win !!!!!")
    elif (a == 3 and b==2): 
        print("you loose ....")
    elif (a==b):    
        print('''match is tie please try again......''')
    else:   
        print("wrong input...")

    
    if (b == 4):
        print("thanks for visiting")
        break

    if (a==1):  
        print("your opponent choice is ROCK")
    elif (a==2):
        print("your opponent choice is PAPER")
    else:
        print("your opponent choice is SCISSOR")

    print('\n')