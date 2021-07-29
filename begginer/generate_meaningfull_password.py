import random 

print("Wel-Come to password generator !!!")
p_bio = []
a_bio = []
s_bio = ["!","@","#","$","%","^","&","*"]
num = ["112","323","456","884","512","021","12"]

name = raw_input("enter your name : ")
p_bio.append(name)

sirname = raw_input("enter your sirname : ")
p_bio.append(sirname)

phone = raw_input("first two digit of your mobile number : ")
p_bio.append(phone)

date = raw_input("enter your date of birth (in the form of 'dd') : ")
a_bio.append(date)

month = raw_input("enter your birth month (in the form of 'jan,feb....')  : ")
a_bio.append(month)

year = raw_input("enter your birth year (in the form of 'yyyy')  : ")
a_bio.append(year)

middle_name = raw_input("enter your middle name : ")
a_bio.append(name)

final = []

pass_p = random.choice(p_bio)
pass_a = random.choice(a_bio)
pass_s = random.choice(s_bio)
pass_n = random.choice(num)

password_1 = pass_p + pass_a + pass_s + pass_n
password_2 = pass_n + pass_s + pass_p + pass_a
password_3 = pass_a + pass_s + pass_n + pass_p

final.append(password_1)
final.append(password_3)
final.append(password_2)

password = random.choice(final)

print("your password is : ")
print(password)
