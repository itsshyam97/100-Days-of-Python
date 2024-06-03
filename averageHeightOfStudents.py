# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

sum = 0
count = 0

for i in student_heights:
  sum += i
  count += 1

number_of_students = count
average_height = round(sum / number_of_students)

print(f'total height = {sum}\nnumber of students = {number_of_students}\naverage height = {average_height}')