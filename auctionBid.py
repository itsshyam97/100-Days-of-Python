import os
import art

print(art.logo2)

dict = {}
high = 0
high_name = ''

end = False

while not end:

    name = input('what\'s your name? : ')
    bid = int(input("what's your bid? :$"))

    dict[name] = bid
    choice = input('is there any other bidder, type "yes" or "no": ')

    os.system('cls')

    if choice == 'no':
        end = True
        for i in dict:
            if dict[i] > high:
                high = dict[i]
                high_name = i

        print(f'{high_name} has highest bid of ${dict[high_name]}')
    
        