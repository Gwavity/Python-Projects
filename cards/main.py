from card import Card
import player
from deck import cardDeck

deck = cardDeck()

if __name__ == "__main__":
    while True:
        try:
            playerCount = int(input("Enter how many players (Max 4): "))
            if playerCount not in range(1,5):
                playerCount = int(input("Enter how many players (Max 4): "))
            else:
                break 
        except Exception as e:
            if type(e) == ValueError:
                print("Please enter a number.\n")
    
    for i in range(playerCount):
        player.Player(input("Enter your name: "))

    deck.createDeck()
    
    currentPlayerIter = 0
    
    deck.shuffle()
    
    for cards in deck.deck:
        curerntPlayer = list(player.players[currentPlayerIter].keys())[0]
        curerntPlayer.giveCard(cards)
        currentPlayerIter += 1
        
        if currentPlayerIter >= len(list(player.players)):
            currentPlayerIter = 0
    
    for _ in player.players:
        for k,v in _.items():
            print(f"{k.name}: {', '.join(deck.printDeck(v))}")
    
    print("")
    deck.clear()

    for cards in deck.deck:
        curerntPlayer = list(player.players[currentPlayerIter].keys())[0]
        curerntPlayer.giveCard(cards)
        currentPlayerIter += 1
        
        if currentPlayerIter >= len(list(player.players)):
            currentPlayerIter = 0
    
    for _ in player.players:
        for k,v in _.items():
            print(f"{k.name}: {', '.join(deck.printDeck(v))}")
