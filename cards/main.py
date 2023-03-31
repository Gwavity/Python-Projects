from card import Card
import player
from deck import cardDeck

# player = Player()
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
        
    # newPlayer = player.Player("John")

    # deck.createDeck()

    # print(" ".join(deck.printDeck(deck.deck)) + "\n")
    # for i,card in enumerate(deck.deck.copy()):
    #     if i >= 5:
    #         break
    #     print(f"Giving {newPlayer.name} {card.toString()}")
    #     newPlayer.giveCard(card)
    #     deck.removeCard(card)
    
    # print(deck.printDeck(deck.deck))

    
    for i in range(1):
        player.Player(input("Enter your name: "))
        # player.Player("Jake")
        # player.Player("Alex")
        # player.Player("Mike")

        
        # player.addPlayer("a")#playerName=input("Enter your name: "))

    # print(player.players)
    deck.createDeck()
    
    currentPlayerIter = 0
    
    deck.shuffle()
    
    for cards in deck.deck:
        curerntPlayer = list(player.players[currentPlayerIter].keys())[0]

        # if cards.rank == "ACE":
        #     choice = input(f"Since {curerntPlayer.name} got an ACE, would you like ")

        curerntPlayer.giveCard(cards)
        currentPlayerIter += 1
        if currentPlayerIter >= len(list(player.players)):
            currentPlayerIter = 0
    
    for _ in player.players:
        for k,v in _.items():
            print(f"{k.name}: {', '.join(deck.printDeck(v))}")
    
    print("")
    deck.clear()

    # print(deck.printDeck(deck.deck))
    for cards in deck.deck:
        curerntPlayer = list(player.players[currentPlayerIter].keys())[0]

        # if cards.rank == "ACE":
        #     choice = input(f"Since {curerntPlayer.name} got an ACE, would you like ")

        curerntPlayer.giveCard(cards)
        currentPlayerIter += 1
        if currentPlayerIter >= len(list(player.players)):
            currentPlayerIter = 0
    
    for _ in player.players:
        for k,v in _.items():
            print(f"{k.name}: {', '.join(deck.printDeck(v))}")
        

    

        # print(_.cards)
    
    # for _ in
    # for _ in len()