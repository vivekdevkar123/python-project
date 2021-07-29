email = raw_input("enter your email address : ")
a = email.find("@")

user = str(email[0:a])
domain = str(email[a+1:])
print("username --> " + user)
print("domain --> " + domain)