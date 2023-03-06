from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

#Faster because instead of pulling from the Minecraft API it scrapes the site with selenium.

class getMC:
    def __init__(self) :
        self.url = "https://namemc.com/profile/"
        self.uuid = []
        self.html = None
        self.username = None
        self.imageLink = None
    
    def retrieveIMG(self):
        self.imageLink = f"https://mc-heads.net/player/{self.username}/128.png"
        return self.imageLink

    def retrieveUsername(self):
        main = self.html.find("main",class_="container")
        self.username = main.find("h1").text

        self.retrieveIMG()
        return self.username

    def retrieveUUID(self):
        card = self.html.find("div",class_="card-body py-1")

        if card == None:
            return None

        for k,v in enumerate(card.children):
            if "samp" in str(v):
                ok = v.find("samp")
                self.uuid.append(ok.text)

        self.retrieveUsername()
        return self.uuid
    
    def getHTML(self,username):
        url = self.url + username
        self.username = username
        driver = uc.Chrome()
        driver.get(url)

        elem = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME, "container")))
        html = driver.page_source
        soup = BeautifulSoup(html,"html.parser")

        self.html = soup
        uuid = self.retrieveUUID()
        driver.quit()
        if uuid == None:
            return f"`Can't find user: {self.username}`"
        return uuid,self.username,self.url + self.username,self.imageLink
