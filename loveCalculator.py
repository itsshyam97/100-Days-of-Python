print("The Love Calculator is calculating your score...")
name1 = input('what is your name? : ') # What is your name?
name2 = input('what is their name? : ') # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = (name1 + name2).upper()

first = name.count('T') + name.count('R') + name.count('U') + name.count('E') 
second = name.count('L') + name.count('O') + name.count('V') + name.count('E') 

total = str(first) + str(second)

final = int(total)

if final < 10 or final > 90:
  print(f'Your score is {final}, you go like coke and mentos')
elif final < 50 and final > 40:
  print(f'Your score is {final}, you are alright together.')
else:
  print(f'Your score is {final}.')
