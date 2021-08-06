special_charactor = ["!","@","#","$","%","^","&","*","<",">","?"]
capital_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
password = raw_input("Enter your password --> ")


if (len(password) >= 8):
    score = 0
    for i in password:
        if i in special_charactor:
            score += 1
        if i in capital_alphabet:
            score += 1
        if i in numbers:
            score += 1
    if (score == 0):
        print("Weak")
    elif (score == 1):
        print("storong")
    elif (score == 2):
        print("very strong")
    elif (score == 3):
        print("very very strong")
else:
    print("very weak please set another password")
            
            
            
        
