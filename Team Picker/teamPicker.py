import random

names = input('Enter the names of people playing(split up by commas): ')
teamDic = {'T1':'','T2':''}
namesList = names.split(',')

if len(namesList) % 2 == 0:
    pass
else:
    print('Please enter an even amount of player names.')
    exit()

while len(namesList):
    random_name = random.choice(namesList)
    if len(namesList) % 2 == 0:
        teamDic['T1'] += random_name.capitalize() + ' '
    else:
        teamDic['T2'] += random_name.capitalize() + ' '
    namesList.remove(random_name)

for t1,names in teamDic.items():
    print(t1 + ': ' + names)
