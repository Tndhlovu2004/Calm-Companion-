import json

try:
    with open("name.json", "r") as file:
        name = json.load(file)
except FileNotFoundError:
    name = input("Hi! What is your name?")

print("----------CALM COMPANION------------")

print("1. Encouragement.")
print("2. Breathing excercise.")
print("3. Bible Verse.")

option = int(input(f"Hi {name}, what do you need right now?"))


