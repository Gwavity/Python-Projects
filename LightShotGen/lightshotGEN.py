import webbrowser,string,random

def generateandsendlink(amount):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'# Just so your history doesn't get spammed with random screenshot links.
    characters = string.ascii_lowercase + string.digits
    link = random.choice(characters)
    print(link)
    if link == '0':
        link = random.choice(characters)
    for i in range(amount):
        print(link)
        if len(link) == 6:
            webbrowser.get(chrome_path).open('https://prnt.sc/' + link)# If you don't care about your history getting spammed with random links, you can remove the "chrome_path" variable above and replace this line with "webbrowser.open('https://prnt.sc/' + link)"
            link = random.choice(characters)
        link += random.choice(characters)

def amountdetermination(amount):
    while amount <= 0:
        print('Please enter a number above 0.')
        amount = int(input('How many times would you like to generate a new Lightshot link? '))
    if amount < 10:
        amount = amount * 6
    else:
        amount = (amount * 6) - 6
    generateandsendlink(amount)

tabNumber = int(input('How many times would you like to generate a new Lightshot link? '))
amountdetermination(tabNumber)
