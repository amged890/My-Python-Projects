def login(username, password):
    users = {}
    file = open("user.txt", "r")
    for lines in file:
        temp = lines.strip().split(", ")
        #print(temp)
        user = temp[0]
        passw = temp[1]

        users[user] = passw
    #print(users)

    if username not in users:
        print("This username does not exist!")
    elif password != users[username]:
        print("Your password is incorrect!")
    else:
        print(f"Welcome {username}")

print("Welcome! Please login with your details!")
while 1:
    username = input("please enter your username!:  ")
    password = input("please enter your password!:  ")
    login(username,password)