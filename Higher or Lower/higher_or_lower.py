import random
from art import logo, vs
from game_data import data


#get random entry A from game data

#print entry A with key value pairs

#get a second random entry B from game data, make sure it's different from the first

#compare entry A and entry B, what has the highest follower count? entry A or B.. make all answers uppercase to mitigate errors

#if correct change entry A to correct answer

#get a random entry B from game data

#compare to entry 1

#if incorrect end game, display number of correct answers. 

#ask if user would like to play again?

print(logo)


play = True

correct = 0

entry_a = {}
entry_b = {}
def draw_entries():
    global entry_a
    global entry_b
    entry_a = random.choice(data)
    entry_b = random.choice(data)
    if entry_a == entry_b:
        draw_entries()
    else:
        return entry_a, entry_b

def print_entries(entry_a, entry_b):
    print(f"Compare A: {entry_a.get('name')}, a {entry_a.get('description')}, from {entry_a.get('country')}")
    print(vs)
    print(f"Compare B: {entry_b.get('name')}, a {entry_b.get('description')}, from {entry_b.get('country')}")

def compare_entries(entry_a, entry_b):
    if 

    

while play:

    def game_play():
        draw_entries()
        print_entries(entry_a, entry_b)
        compare_entries(entry_a, entry_b)

    game_play()


