import requests

#Faster because instead of scraping the site with beatifulSoup and selenium, it just makes a reuqest to the minecraft API

class getMC:
    def __init__(self,username):
        self.url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
        self.username = username
    
    def retrieveIMG(self):
        return f"https://mc-heads.net/player/{self.username}/128.png"
    
    def retrieveUser(self):
        return requests.get(f"https://api.mojang.com/users/profiles/minecraft/{self.username}")
    
    def run(self):
        user = self.retrieveUser()
        image = self.retrieveIMG()
        return user, image
