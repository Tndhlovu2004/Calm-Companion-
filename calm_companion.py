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
    print()
    time.sleep(4)

 print("Please talk to someone if you need to. It's okay to seek help. You don't have to face these feelings alone.")
 print()

 input("Press enter to return to the menu.")

def breathing_excercise():

    print("Gently take a breath in. ")
    time.sleep(3)
    print("Gently breathe out. ")
    time.sleep(3)
    print("Gently take a breath in. ")
    time.sleep(3)
    print("Gently breathe out. ")
    time.sleep(3)

def bible_verse():

   bible_verses = ["Philipians 4:6: Do not be anxious or worried about anything, "
   "but in everything by prayer and petition with thanksgiving, make your requests known to God.", 
   "1 Peter 5:7: Casting all your cares on Him, for He cares about you.",
   "Isaiah 41:10: Do not fear anything, for I am with you; Do not be afraid, for I am your God. I wil strengthen"
   "you, be assured I will help you; I will certainly take hold of you with my righteous right hand.",
   "God is with you, he loves you and he will help you get through this."]

   for verse in bible_verses:
      print(verse)
      print()
      time.sleep(4)

   print("I encourage you to pray to God and bring your feelings to him.")
   print()
   print("Please talk to someone if you need to. It's okay to seek help. You don't have to face these feelings alone.")
   print()

   input("Press enter to return to the menu.")

while True:
 
 print("----------CALM COMPANION------------")

 print("1. Encouragement.")
 print("2. Breathing excercise.")
 print("3. Bible Verse.")

 option = int(input(f"Hi {name}, what do you need right now?"))

 if option == 1:
    encouragement()
 elif option == 2:
    breathing_excercise()
 elif option == 3:
    break




