from Blackjack_methods import Deck
#variables
d = 6
player = Deck(d)
dealer = Deck(d)
playerLeftHand = Deck(d)
playerRightHand = Deck(d)
splitter = 0
blackjack = 0
objects = (player, dealer, playerLeftHand, playerRightHand)

#Questioning
initial_Balance = int(input('How much money will we be playing with today? '))
if initial_Balance == '...':
    d = int(input('How many decks do you want to play with? '))

#Game
while initial_Balance > 0:
    skip = 0
    blackjack = 0
    bet = input('Place your bets? ')
    if bet == 'quit':
        print('Thanks for playing! ')
        quit()
    bet = int(bet)
    while bet <= 0 or initial_Balance - bet < 0:
        bet = int(input('Please use a positive integer and your balance is at least 0 after this bet! '))
    initial_Balance -= bet
    print(initial_Balance)
    
    # Dealer cards dealt
    print('The dealer has a: ')
    dealer.move()
    if sum(dealer.showNumHand()) == 11:
        secondDCard = dealer.random()
        dealer.hand(dealer.rankCorrection(dealer.showNumHand()), dealer.rank())
        insurance = input('Would you like to take insurance? ')
        if insurance == 'yes':
            num = int(input('How much insurance do you want to buy? '))
            initial_Balance -= num
        if sum(dealer.showNumHand()) == 21:
            print('Dealer Wins: BlackJack')
            if insurance == 'yes':
                initial_Balance = insurance * 2
            blackjack = 1

    # Player cards dealt
    print('Your cards are: ')
    for _ in range(2):
        player.move()
    print(f'The player\'s total is {player.showTotal()}')
    if player.showTotal() == 21:
        blackjack = 1
        print('Blackjack!')
        dealer.move()
        print(f'The dealer\'s total is {dealer.showTotal()}')

        #Blackjack Endgame
        if sum(player.showNumHand()) == sum(dealer.showNumHand()):
            print('Push')
            initial_Balance += bet
            for i in objects:
                i.clearHands()
            
        elif dealer.bust(dealer.showNumHand()) and len(dealer.showNumHand()) >= 1:
            print('You win: Dealer Busted')
            initial_Balance += bet * 2
            for i in objects:
                i.clearHands()

        elif player.beat(player.showNumHand(), dealer.showNumHand()) and len(dealer.showNumHand()) >= 1:
            print('You win')
            initial_Balance += bet * 2
            for i in objects:
                i.clearHands()
        
        elif dealer.beat(dealer.showNumHand(), player.showNumHand()) and len(dealer.showNumHand()) >= 1:
            print('You lose')
            for i in objects:
                i.clearHands()

    
    # Players Choice
    if blackjack == 0:
        choice = input('What is your move? ')
        while choice != 'split' and choice != 'hit' and choice != 'double' and choice != 'stand':
            choice = input('Please keep all characters in lower case and choose either \'hit\', \'stand\', \'double\', or \'split\' ')
        while choice == 'split' and player.showHand()[0] != player.showHand()[1]:
            choice = input('You can not split on this hand because your cards ranks do not macth! ')

        # Mid Game/player's side
        while True:
            if splitter == 0:
                x = player
                times = 1
            elif splitter == 1:
                x = playerLeftHand
                times = 2
            elif splitter == 2:
                x = playerRightHand
            if choice == 'hit':
                x.move()
                print(f'The player\'s total is {x.showTotal()}')
                if x.bust(x.showNumHand()):
                    print('You lose: busted')
                    if x == player:
                        skip = 1
                    elif playerRightHand.bust(x.showNumHand) and playerLeftHand.bust(playerLeftHand.showNumHand()):
                        skip = 1
                    if x == playerLeftHand:
                        splitter += 1
                        choice = input('What is your move for your right hand? ')
                        continue
                    for i in objects:
                        i.clearHands()
                    break
                elif sum(x.showNumHand()) == 21:
                    print('You made 21! ')
                    if x == playerLeftHand:
                        splitter += 1
                        choice = input('What is your move for your right hand? ')
                        continue
                    break
                else:
                    choice = input('What is your move? ')
                    continue
            
            elif choice == 'stand':
                if x == playerLeftHand:
                    splitter += 1
                    choice = input('What is your move for your right hand? ')
                    continue
                break

            elif choice == 'double':
                if len(x.showNumHand()) == 2 or (initial_Balance - bet) < 0:
                    initial_Balance -= bet            
                    bet *=2
                    x.move()
                    print(f'The player\'s total is {x.showTotal()}')
                    if x.bust(x.showNumHand()):
                        print('You lose: busted')
                        skip = 1
                        if x == playerLeftHand:
                            splitter += 1
                            choice = input('What is your move for your right hand? ')
                            continue
                        for i in objects:
                            i.clearHands()
                    elif sum(x.showNumHand()) == 21:
                        print('You made 21! ')
                        if x == playerLeftHand:
                            splitter += 1
                            choice = input('What is your move for your right hand? ')
                            continue
                    break
                else:
                    choice = input('You can not double because you have more then two cards or you do not have enough balance, please \'hit\' or \'stand\' ')
                    continue
                
            elif choice == 'split':
                playerLeftHand.hand(player.showNumHand()[0], player.rank())
                playerRightHand.hand(player.showNumHand()[1], player.rank())
                playerLeftHand.move()
                print(f'Your left hand Total is {playerLeftHand.showTotal()}')
                playerRightHand.move()
                print(print(f'Your right hand Total is {playerRightHand.showTotal()}'))
                splitter += 1
                choice = input('What is your move for your left hand? ')

        #Midgame/Dealer's side
        if skip == 0:
            while sum(dealer.showNumHand()) < 17 and len(dealer.showNumHand()) >= 1:
                dealer.move()
            print(f'The dealer\'s total is {dealer.showTotal()}')

            #Endgame
            for i in range(times):
                if i == 0 and times == 1:
                    x = player
                elif i == 0 and times == 2:
                    x = playerLeftHand
                elif i == 1 and times == 2:
                    x = playerRightHand
                if sum(x.showNumHand()) == sum(dealer.showNumHand()):
                    print(f'{x} Push')
                    initial_Balance += bet
                    for i in objects:
                        i.clearHands()
                    
                elif dealer.bust(dealer.showNumHand()) and len(dealer.showNumHand()) >= 1:
                    print(f'{x} win: Dealer Busted')
                    initial_Balance += bet * 2
                    for i in objects:
                        i.clearHands()

                elif x.beat(x.showNumHand(), dealer.showNumHand()) and len(dealer.showNumHand()) >= 1:
                    print(f'{x} win')
                    initial_Balance += bet * 2
                    for i in objects:
                        i.clearHands()
                
                elif dealer.beat(dealer.showNumHand(), player.showNumHand()) and len(dealer.showNumHand()) >= 1:
                    print(f'{x} lose')
                    for i in objects:
                        i.clearHands()
