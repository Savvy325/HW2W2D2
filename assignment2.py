# 1. Nested Decisions: The Adventure Game

#Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
else: 
    if place == "cave":
        print("You find a hidden treasure!")

#Task 2: Setting the Scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Yay! I saw this hole and didn't fall!")
    if action == "proceed in the dark":
        print("Oh no! I fell and broke my leg")

# Task 3: Default Path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Yay! I saw this hole and didn't fall!")
    if action == "proceed in the dark":
        print("Oh no! I fell and broke my leg")
else:
    pass

# 2. Quick Decisions: The Event Planner

# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection
if venue == "large hall":
    print("projector")
elif venue == "conference room":
    print("audio system")

# Task 3: Catering Choices
food = input("Are you a vegetarian? (yes/no)")
if food == "yes":
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")