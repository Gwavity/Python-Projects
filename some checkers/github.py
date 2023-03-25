import requests
import random
import colorama
from multiprocessing.pool import ThreadPool
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
fileLength = 0
errorCount = 0
nameFile = "2chars.txt" #Ex. nameslist.txt

def saveValidUser(username):
    with open("newNames.txt","a") as newnames:
        newnames.write(f"{username}\n")

def saveCurrentTextFile():
    with open(nameFile,"w+") as replace:
        replace.writelines(otherList.copy())
    os._exit(1)

def checkUser(username):
    global increment
    global otherList
    global errorCount

    headers = {
        "User-Agent": random.choice(users)
    }

    name = username.strip().lower()
    ok = requests.get(f"https://github.com/{name}/",headers=headers)

    if errorCount >= 20:
        saveCurrentTextFile()

    if ok.status_code == 429:
        if increment == 0:
            print("broken")
            os._exit(1)

        print("broken",increment)
        errorCount += 1
        return

    if ok.status_code != 200:
        print(f"{colorama.Fore.GREEN}{name}, is available, {ok.url}\n")
        saveValidUser(name)
        otherList.remove(username)
    else:
        pass
        print(f"{colorama.Fore.RED}{name}, is not available, {ok.url}\n")
        otherList.remove(username)

    increment += 1

with open(nameFile,"r") as names:
    open("newNames.txt","w").close()

    nameList = names.readlines()
    fileLength = len(nameList)
    otherList = nameList
    pool = ThreadPool()

    results = pool.map(checkUser,nameList)
    
print(increment)

if increment == fileLength:
    print(f"{colorama.Fore.GREEN}\n\n-------------------------\n\nFINISHED CHECKING FILE\n\n-------------------------\n\n\n")
