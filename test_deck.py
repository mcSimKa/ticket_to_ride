import unittest
from carddeck import CardDeck


class MyTestCase(unittest.TestCase):
    def test_create_deck(self):
        card_deck = CardDeck()
        card_deck.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'A']
        hand = card_deck.deal_cards(5)
        self.assertEqual([1,2,3,4,5],hand)
        self.assertEqual(9, len(card_deck.deck))


if __name__ == '__main__':
    unittest.main()
