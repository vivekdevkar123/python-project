a_string = list(raw_input("enter your sentence : ").upper().split(" "))
print(list(a_string))

for character in a_string:
    if character[0].isalnum():
        sen.append(character)

ans = []
for i in sen:
    ans.append(i[0])
    
print("".join(ans))
