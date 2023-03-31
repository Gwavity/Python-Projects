from card import Card
import player
import random

class cardDeck:
    def __init__(self):
        self.deck = []
    
    def createDeck(self):
        self.deck = []

        for suits in Card().cardSuits:
            for ranks in Card().cardRanks:
                self.deck.append(Card(suits,ranks))
        
        print(f"The deck now has {self.count()} cards.\n")

    def count(self):
        return len(self.deck)
    
    def clear(self):
        self.deck.clear()
        for i in player.players:
            for cards in i.values():
                cards.clear()
        self.createDeck()
    
    def shuffle(self):
        shuffleAmount = random.randint(100,1001)
        msg = f"Shuffling deck {shuffleAmount} times."
        print(f"{len(msg) * '-'}\n{msg}\n{len(msg) * '-'}\n")

        for _ in range(shuffleAmount):
            initial = random.randint(0,len(self.deck) - 1)
            final = random.randint(0,len(self.deck) - 1)
            if initial == final:
                continue
            self.move(initial,final)
        return

    def move(self,initial,final):
        temp = self.deck[initial]
        self.deck[initial] = self.deck[final]
        self.deck[final] = temp

        return 0
    
    def removeCard(self,card):
        self.deck.remove(card)
        return

    def printDeck(self,deck):

        return [card.toString() for card in deck]
    
    def printBackwards(self,deck):

        return [card.toString() for card in reversed(deck)]
