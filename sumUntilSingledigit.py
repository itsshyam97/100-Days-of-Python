number = input('enter a number : ')
length = len(number)
sum = 0
if length == 2:
	sum = int(number[0]) + int(number[1])
while length > 2:
	for i in range (0,length):
		# print(number[i])
		sum += int(number[i])
	number = str(sum)
	length = len(number)
while len(str(sum)) == 2:
	newsum = str(sum)
	sum = int(newsum[0]) + int(newsum[1])

print(sum)