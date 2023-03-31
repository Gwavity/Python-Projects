players = []

def clearPlayers():
    players.clear()

class Player:
    def __init__(self,name):
        self.cards = []
        self.name = name
        players.append({self:self.cards})
    
    def giveCard(self,card):
        self.cards.append(card)
