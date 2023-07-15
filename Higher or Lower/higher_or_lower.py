import random
from art import logo, vs
from game_data import data

print(logo)


play = True

correct = 0
compare_again = True
entry_a = {}
entry_b = {}
winning_entry = ""
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
    global winning_entry
    global user_choice
    if entry_a['follower_count'] > entry_b['follower_count']:
        winning_entry = entry_a
    elif entry_a['follower_count'] < entry_b['follower_count']:
        winning_entry = entry_b
    user_choice = input("Who has more followers?: A or B ")
    user_choice = user_choice.upper()
    if user_choice == "A":
        user_choice = entry_a
    elif user_choice == "B":
        user_choice = entry_b 
    return winning_entry, user_choice

def pick_winner(winning_entry, user_choice):
    global compare_again
    global correct
    global entry_a
    if user_choice == winning_entry:
        print("That is correct!")
        entry_a = winning_entry
        correct += 1
        print(f"You have {correct} correct so far")
        return entry_a
    else:
        print("I'm sorry, that is incorrect")
        print(f"You got {correct} correct")
        compare_again = False

def getting_entry_b(entry_a):
    global entry_b
    entry_b = random.choice(data)
    if entry_b == entry_a:
        entry_b = random.choice(data)
    else:
        return entry_b
    
def second_round(winning_entry, entry_a):
    while compare_again:
        getting_entry_b(entry_a)
        print_entries(entry_a, entry_b)
        compare_entries(entry_a, entry_b)
        pick_winner(winning_entry, user_choice)


def game_play():
        draw_entries()
        print_entries(entry_a, entry_b)
        # while compare_again:
        compare_entries(entry_a, entry_b)
        pick_winner(winning_entry, user_choice)
        if compare_again == True:
            second_round(winning_entry, entry_a)
        else:
            print("Thank you for playing, better luck next time")
        

game_play()


