from carddeck import CardDeck

class Player():
    def __init__(self):
        self.hand = []
        self.card_deck = None

    def show_hande(self):
        return self.hand

    def join_game(self, card_deck : CardDeck):
        self.card_deck = card_deck

    def take_card(self, number : int) -> bool:
        if not self.card_deck is None:
            return False
        else:
            self.hand.append(self.card_deck.)
