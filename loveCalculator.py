print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
comined_name = name1 + name2
comined_name_lowercase = comined_name.lower()
t = comined_name_lowercase.count("t")
r = comined_name_lowercase.count("r")
u = comined_name_lowercase.count("u")
e = comined_name_lowercase.count("e")
first_digit = t + r + u + e
l = comined_name_lowercase.count("l")
o = comined_name_lowercase.count("o")
v = comined_name_lowercase.count("v")
e = comined_name_lowercase.count("e")
second_digit = l + o + v + e

final_score = int(str(first_digit) + str(second_digit))
if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score > 40 and final_score < 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
