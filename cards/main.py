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
        curerntPlayer = player.players[currentPlayerIter]

        curerntPlayer.giveCard(cards)
        currentPlayerIter += 1
        if currentPlayerIter >= len(list(player.players)):
            currentPlayerIter = 0
    
    for _ in player.players:
        print(f"{_.name}: {', '.join(deck.printDeck(_.cards))}")
    
    print("")
    deck.clear()

    currentPlayerIter = 0

    for cards in deck.deck:
        curerntPlayer = player.players[currentPlayerIter]
        print(curerntPlayer.name, print(cards.toString()))

        curerntPlayer.giveCard(cards)
        currentPlayerIter += 1
        if currentPlayerIter >= len(list(player.players)):
            currentPlayerIter = 0
    
    for _ in player.players:
        print(f"{_.name}: {', '.join(deck.printDeck(_.cards))}")
