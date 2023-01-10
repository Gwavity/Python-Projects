from selenium import webdriver
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self):
        self.url = "https://what-to-code.com/random"
        self.driver = webdriver.Chrome()

    def RetreiveCodeIdea(self):
        while True:
            driver = self.driver
            driver.get(self.url)
            html = driver.page_source
            soup = BeautifulSoup(html,"html.parser")
            card = soup.find_all("div",class_="card Idea_idea___srOn")
            try:
                cardContent = card[0].find("div",class_="card-content")
                header = cardContent.find("p",class_="has-text-weight-bold is-size-5")
                body = cardContent.find("p",class_="subtitle")
                return header.text,body.text
            except Exception as e:
                if type(e) == IndexError:
                    print(e)
                    continue
