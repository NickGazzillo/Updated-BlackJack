class Deck:
    def __init__(self, d):
        self._rank = None
        self._suit = None
        self._decks = d
        self._played = {'Hearts':{5:0}, 'Diamonds':{5:0}, 'Clubs':{5:0}, 'Spades':{5:0}}
        '''{'Hearts':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Clubs':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Diamonds':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0},
        'Spades':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}}'''
        self._count = 0
        self._hand = []
        self._numHand = []

    def random(self):
        import random as r
        _ranks = [5]
        _suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        '[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]'
        
        self._rank = r.choice(_ranks)
        self._suit = r.choice(_suits)
        if self._played[self._suit][self._rank] < self._decks * 4:
            self._played[self._suit][self._rank] += 1
            self._count += 1 
        else:
            while self._played[self._suit][self._rank] >= 24:
                self._rank = r.choice(_ranks)
                self._suit = r.choice(_suits)
            self._played[self._suit][self._rank] += 1
            self._count += 1 
        card =  f'{self._rank} of {self._suit}'
        if self._count == 52 * self._decks:
            self._played = {'Hearts':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Clubs':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Diamonds':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0},
        'Spades':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}}
            print('No more cards left, reshuffling deck')
        return card
    
    def rankCorrection(self, n):
        if self._rank == 'Jack':
            return 10
        if self._rank == 'Queen':
            return 10
        if self._rank == 'King':
            return 10
        if self._rank == 'Ace':
            if sum(n) > 21:
                return 1
            else:
                return 11
        return self._rank
    
    def rank(self):
        return self._rank

    def bust(self, pn:list):
        return sum(pn) > 21    

    def beat(self,pn:list,dn:list):
        '''
        True = player win
        False = Player loss
        None = push
        '''
        sumP = sum(pn)
        sumD = sum(dn)
        if sumP <= 21 and sumP > sumD:
            return True
        elif sumD <= 21 and sumP < sumD:
            return False
        elif sumP == sumD and sumP <= 21:
            return 'Push'

    def display(self):
        print(f'{self._rank} of {self._suit}')
    
    def hand(self, n:int, s:str):
        self._hand.append(s)
        self._numHand.append(n)

    def showHand(self):
        return self._hand

    def showNumHand(self):
        if sum(self._numHand) > 21 and self._numHand.count(11) > 0:
            if self._numHand.count(11) == 1:
                 self._numHand[self._numHand.index(11)] = 1
            else:
                for _ in range(self._numHand.count(11)):
                    self._numHand[11] = 1
        return self._numHand

    def showTotal(self):
        return sum(self.showNumHand())

    def move(self):
        self.random()
        self.hand(self.rankCorrection(self.showNumHand()), self.rank())
        self.display()
    
    def clearHands(self):
        self._hand.clear()
        self._numHand.clear()           

class Simulation:
    def __init__(self, d):
        self._rank = None
        self._suit = None
        self._decks = d
        self._played = {'Hearts':{5:0}, 'Diamonds':{5:0}, 'Clubs':{5:0}, 'Spades':{5:0}}
        '''{'Hearts':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Clubs':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Diamonds':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0},
        'Spades':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}}'''
        self._count = 0
        self._hand = []
        self._numHand = []
        self._dealer = []

    def random(self):
        import random as r
        _ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        _suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        '[2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]'
        
        self._rank = r.choice(_ranks)
        self._suit = r.choice(_suits)
        if self._played[self._suit][self._rank] < self._decks * 4:
            self._played[self._suit][self._rank] += 1
            self._count += 1 
        else:
            while self._played[self._suit][self._rank] >= 24:
                self._rank = r.choice(_ranks)
                self._suit = r.choice(_suits)
            self._played[self._suit][self._rank] += 1
            self._count += 1 
        card =  f'{self._rank} of {self._suit}'
        if self._count == 52 * self._decks:
            self._played = {'Hearts':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Clubs':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}, 
        'Diamonds':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0},
        'Spades':{2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, "Jack":0, "Queen":0, "King":0, "Ace":0}}
            print('No more cards left, reshuffling deck')
        return card

    def hit(self):
        for _ in range(100_000):
            self.random()
