import random

while True:
    print("Enter 1 for roll")
    print("Enter 0 for exit")
    a = int(input("Choice --> "))
    if (a == 1):
        random_number = random.randrange(1,7)
        print(random_number)
    elif (a == 0):
        break
    else:
        print("Select a valid option")

    print(" ")