import json
import time

try:
    with open("name.json", "r") as file:
        name = json.load(file)
except FileNotFoundError:
    name = input("Hi! What is your name?")

    with open("name.json", "w") as file:
        json.dump(name, file)

def encouragement():

 messages = ["You are not defined by your anxiety. Remember that.", 
            "There is nothing wrong with you for feeling this way.",
            "Things feel hard right now, but you won't feel this way forever.",
            "You are strong and you can overcome this feeling."]

 for message in messages:
    print(message)
    time.sleep(4)

def bible_verse():

   bible_verses = ["Philipians 4:6: Do not be anxious or worried about anything, "
   "but in everything by prayer and petition with thanksgiving, make your requests known to God.",
   "1 Peter 5:7: Casting all your cares on Him, for He cares about you.",
   "Do not fear anything, for I am with you; Do not be afraid, for I am your God. I wil strengthen"
   "you, be assured I will help you; I will certainly take hold of you with my righteous right hand."]

   for verse in bible_verses:
      print(verse)
      time.sleep(4)

print("----------CALM COMPANION------------")

print("1. Encouragement.")
print("2. Breathing excercise.")
print("3. Bible Verse.")

option = int(input(f"Hi {name}, what do you need right now?"))




