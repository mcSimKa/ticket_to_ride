import random

class CardDeck:
    def __init__(self):
        self.deck = []
        pass

    def shuffle(self):
        random.shuffle(self.deck)
        return True

    def deal_cards(self, amount : int) -> list:
        split = min(amount, len(self.deck))
        result = []
        if split > 0:
            result, self.deck = self.deck[0:split], self.deck[split:]
        return result

    def __str__(self):
        return str(self.deck)

