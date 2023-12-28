def rps_game():
    import random as rd

    cpu_choice = rd.randint(1, 3)
    user_choice = int(input("Rock = 1, paper = 2, scissors = 3:\n"))

    if cpu_choice == user_choice:
        print("it's a tie!")
    elif cpu_choice == 1 and user_choice == 2:
        print("You win!")
    elif cpu_choice == 1 and user_choice == 3:
        print("I win!")
    elif cpu_choice == 2 and user_choice == 1:
        print("I win!")
    elif cpu_choice == 2 and user_choice == 3:
        print("You win!")
    elif cpu_choice == 3 and user_choice == 1:
        print("You win!")
    elif cpu_choice == 3 and user_choice == 2:
        print("I win!")
    else:
        print("Try choosing a number between 1 and 3")


rps_game()
