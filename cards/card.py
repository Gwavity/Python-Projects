class Card:
    def __init__(self,suit= None,rank=None):
        self.suit = suit
        self.rank = rank

        self.cardSuits = ["Hearts"]#"Spades","Diamonds","Clubs"]
        self.cardRanks = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    
    def toString(self):
        rank = self.rank
        if self.rank not in ["Jack","Queen","King","Ace"]:
            cardI = self.cardRanks.index(self.rank) + 1
            rank = cardI

        return f"{rank} of {self.suit}"


# print(card("1","2"))