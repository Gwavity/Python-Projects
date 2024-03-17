from bs4 import BeautifulSoup
from selenium import webdriver
zipCodeInput = input("Enter your zip code: ")
url = f"https://www.bing.com/search?q=gas+near+{zipCodeInput}"
gasStations = {}

driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")    
gasStationIncrement = 0 

feedback = soup.find("div",attrs={"data-feedbk-id":"GasStation"})
items = feedback.find("ol",class_="items")
for i in items:
    strippedList = list(i.stripped_strings)
    if len(strippedList) < 3:
        continue
    if strippedList[0] in gasStations:
        gasStations[strippedList[0] + gasStationIncrement * " "] = [strippedList[1],strippedList[2]]
        gasStationIncrement += 1
    else:
        gasStations[strippedList[0]] = [strippedList[1],strippedList[2]]

newDict = {}
for k in range(len(gasStations)):
    for i,v in gasStations.items():
        stationIndex = list(gasStations.keys()).index(i)
        try:
            nextGassy = list(gasStations.keys())[stationIndex + 1]
        except:
            continue

for i in sorted(gasStations.values()):
    key_list = list(gasStations.keys())
    val_list = list(gasStations.values())

    newKey = val_list.index(i)
    newDict[key_list[newKey]] = i
    
for k,v in newDict.items():
    print(f"{k.strip()}:\nAddress: {v[1]} | Regular gas price: {v[0]}")
