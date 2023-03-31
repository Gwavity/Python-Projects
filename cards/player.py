players = []

def clearPlayers():
    players.clear()

class Player:
    def __init__(self,name):
        self.cards = []
        self.name = name
        players.append(self)
    
    def giveCard(self,card):
        self.cards.append(card)
