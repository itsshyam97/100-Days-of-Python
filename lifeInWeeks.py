age = input("Enter your age : ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

age = int(age)
life_span =  65 - age
weeks_in_an_year =  4 * 1 * 13
remaining_weeks = life_span * weeks_in_an_year

print(f"You have {remaining_weeks} weeks left.")