import requests
import random
import colorama
import threading
import os

users = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
]

increment = 0
otherList = None
nameFile = "2chars.txt" #Ex. nameslist.txt

def saveValidUser(username):
    with open("newNames.txt","a") as newnames:
        newnames.write(f"\"{username}\" could be available\n")

def checkUser(username):
    global broken
    global increment

    headers = {
        "User-Agent": random.choice(users)
    }
    name = username.strip().lower()
    ok = requests.get(f"https://www.grailed.com/{name}",headers=headers)

    if ok.status_code == 429:
        if increment == 0:
            print("Breaking")
            os._exit(1)
            
        print("Broken",increment)
        with open(nameFile,"w") as replace:
            replace.writelines(otherList)
        os._exit(1)

    if ok.status_code == 200:
        print(f"{colorama.Fore.RED}{name}, {ok.status_code}, {ok.url}\n")
    else:
        print(f"{colorama.Fore.GREEN}{name}, {ok.status_code}, {ok.url}\n")
        saveValidUser(name)

    increment += 1
    otherList.remove(username)

threads = []

with open(nameFile,"r+") as names:
    open("newNames.txt","w").close()

    nameList = names.readlines()
    otherList = nameList

    for l in nameList:
        t = threading.Thread(target=checkUser,args=(l,))
        t.daemon = True
        threads.append(t)

for i in threads:
    i.start()

for i in threads:
    i.join()

print(increment)
