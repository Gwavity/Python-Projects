players = []

def clearPlayers():
    players.clear()

class Player:
    def __init__(self,name):
        self.cards = []
        self.name = name
        players.append({self:self.cards})

    # def addPlayer(self,name):
    #     players.append({name:[]})
        # print(players)
    
    def giveCard(self,card):
        self.cards.append(card)
        # cardRemoval = cardDeck().removeCard(card)
        # print(cardRemoval)

    # def printDeck(self):
    #     # for _ in self.cards:
    #     #     print(_.toString())
    #     return [card.toString() for card in self.cards]