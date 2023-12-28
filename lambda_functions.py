greeting = lambda: print("Well Hello There".upper())
custom_greeting = lambda name: print(f"Welcome {name}")
# lambda parameter : expression
add_two = lambda x, y, z: x + y + z


# greeting()

# user_name = input("Please enter your name: ")

# custom_greeting(user_name)

# print(add_two(1, 2, 3))

numbers = [3,5,14,22,25,10]
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

def add_list(list, idx):
    if idx == 0:
        return list[idx]

    return list[idx] + add_list(list, idx - 1)


print(add_list(numbers, 2))
