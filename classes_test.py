# Remember you can import classes to and from other files using " from (file_name) import (class_name)
class Human:

    def __init__(self, name : str , age:int , height:int , fav_beverage: str):
        self.name = name
        self.age = age
        self.height = height
        self.fav_beverage = fav_beverage

    def __str__(self):
        return f"""
Human name : {self.name}
Human age : {self.age}
Human height : {self.height}
Human preferred beverage : {self.fav_beverage}
"""

    def change_age(self, new_age):
        self.age = new_age


human1 = Human("Amged", 22, 183, "Coffee")
human2 = Human("John", 32, 189, "Pepsi")
human3 = Human("Mumbo", 23, 180, "Water")

print(human1, human2, human3)

human3.change_age(30)

print(human3)
