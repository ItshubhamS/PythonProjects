Name = "Shubham"

new_list = [letter for letter in Name]
print(new_list)


new_range = [n * 2 for n in range(1, 5)]
print(new_range)

names = ["Shubham", "rohit", "negi", "vansh", "divyanshu"]
new_names = [name.upper() for name in names if len(name) > 5]
print(new_names)

import random

student_score = {student: random.randint(1, 100) for student in names}

passed_student = {
    student: score for (student, score) in student_score.items() if score > 60
}

print(passed_student)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇
split_sentence = sentence.split()
print(split_sentence)

result = {word: len(word) for word in split_sentence}
print(result)


weather_c = eval(
    '{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}'
)

# 🚨 Don't change code above 👆
weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}

# Write your code 👇 below:


print(weather_f)

import pandas


new_data_frame = pandas.DataFrame(names)


for index, row in new_data_frame.iterrows():
    print(row.student)
