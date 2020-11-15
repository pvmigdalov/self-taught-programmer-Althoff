from random import shuffle

class Card:
    suits = {
        1: 'пикей',
        2: 'червей',
        3: 'бубей',
        4: 'треф'
    }

    values = {
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8', 
        9: '9',
        10: '10',
        11: 'валет',
        12: 'дама',
        13: 'король',
        14: 'туз'
    }

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __it__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            return False
        return False

    def __repr__(self):
        card = self.values[self.value] + ' ' + self.suits[self.suit]
        return card

    def __str__(self):
        return self.__repr__()


class Deck:
    def __init__(self):
        self.cards = [Card(i, j) for i in range(2, 15) for j in range(1, 5)]
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None


class Game:
    def __init__(self):
        name1 = input('Enter your name: ')
        name2 = input('Enter your name: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    
    def wins(self, winner):
        msg = f'{winner} take cards'
        print(msg)

    
    def draw(self, p1n, p1c, p2n, p2c):
        msg = f'{p1n} put {p1c} and {p2n} put {p2c}'
        print(msg)

    
    def play_game(self):
        cards = self.deck.cards
        print('GO! GO! GO!')
        while len(cards) >= 2:
            msg = 'Enter X for quit the game, or any button for play'
            response = input(msg)
            
            if response == 'X' or response == 'x':
                break
           
            p1n = self.p1.name
            p1c = self.deck.rm_card()
            p2n = self.p2.name
            p2c = self.deck.rm_card()
            self.draw(p1n, p1c, p2n, p2c)
            
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(p1n)
            else:
                self.p2.wins += 1
                self.wins(p2n)
       
        win = self.winner(self.p1, self.p2)
        print(f'Game over. {win} win!')

    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.wins
        return 'Nobody wins'

if __name__ == '__main__':
    game = Game()
    game.play_game()
