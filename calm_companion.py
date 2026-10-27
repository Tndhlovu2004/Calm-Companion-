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

 print("Here are some messages of encouragement: ")
 print()

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

def gentle_breathing():

    print("Here is a gentle breathing excercise to help calm your nerves.")
    print()

    print("Gently take a breath in. ")
    time.sleep(3)
    print("Gently breathe out. ")
    time.sleep(3)
    print("Gently take a breath in. ")
    time.sleep(3)
    print("Gently breathe out. ")
    time.sleep(3)

    print("Please talk to someone if you need to. It's okay to seek help. You don't have to face these feelings alone.")
    print()

    print("Press enter to return to the menu.")

def belly_breathing():

   print("Here is a diaphragmatic (belly) breathing excercise to help you relax.")
   print()

   print("Place a hand on your abdomen.")
   time.sleep(3)
   print("Gently breathe in. Watch as your abdomen expands.")
   time.sleep(3)
   print("Gently breathe out. Watch as your abdomen settles.")
   time.sleep(3)
   print("Gently breathe in again. Watch as your abdomen expands once more.")
   time.sleep(3)
   print("Gently breathe in once more. Watch again as your abdomen expands.")
   time.sleep(3)
   print("Gently breathe out again. Watch once more as yoru abdomen settles.")
   time.sleep(3)

   print("I hope you feel a little more at peace.")
   print()
   print("Please talk to someone if you need to. It's okay to seek help. You don't have to face these feelings alone.")
   print()
   print("Press enter to return to the menu.")
 
def bible_verse():

   print("Here are some bible verses to help ease your anxiety.")
   print()

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
 print("2. Gentle-paced breathing excercise.")
 print("3. Belly breathing excercise.")
 print("3. Bible Verse.")

 option = int(input(f"Hi {name}, what do you need right now?"))

 if option == 1:
    encouragement()
 elif option == 2:
    gentle_breathing()
 elif option == 3:
    belly_breathing()
 elif option == 4:




