# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

both_names = (name1_lower + name2_lower)

t_name = both_names.count("t")
r_name = both_names.count("r")
u_name = both_names.count("u")
e_name = both_names.count("e")

first_number = int(t_name + r_name + u_name + e_name)

l_name = both_names.count("l")
o_name = both_names.count("o")
v_name = both_names.count("v")
e_name = both_names.count("e")

second_number = int(l_name + o_name + v_name + e_name)

love_score = str(first_number) + str(second_number)

love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")