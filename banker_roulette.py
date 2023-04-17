# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

length_of_list = len(names)

paying_for_meal = random.randint(0, length_of_list)

name_of_person_paying = names[paying_for_meal]

print(f"{name_of_person_paying} is going to buy the meal today!")
