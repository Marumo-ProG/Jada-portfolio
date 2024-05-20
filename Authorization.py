'''
    in this project we mimic the concept of password protection using loops
    we restrict the user to register with a great password. 
    password must not include some invalid letters if they get it right 
    we display a message
'''
password = input("Enter password:")

forbidden_symbols = "=?*^$№@_,;:#%^&()"

# looking for forbidden symbols in the users password
for letter in password:
    if letter in forbidden_symbols:
        print("Forbidden letter:", letter)
