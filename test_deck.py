import unittest
from carddeck import CardDeck


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.card_deck = CardDeck()
        self.card_deck.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'D', 'K', 'A']

    def test_deal_cards(self):
        hand = self.card_deck.deal_cards(5)
        self.assertEqual([2,3,4,5,6],hand)
        self.assertEqual(8, len(self.card_deck.deck))

    def test_deal_no_cards(self):
        hand = self.card_deck.deal_cards(0)
        self.assertEqual([], hand)
        self.assertEqual(13, len(self.card_deck.deck))

    def test_create_deck(self):
        self.assertEqual([2,3,4,5,6], self.card_deck.deck[0:5])
        self.assertEqual(13, len(self.card_deck.deck))

    def test_shuffle(self):
        self.card_deck.shuffle()
        self.assertNotEqual([2,3,4,5,6], self.card_deck.deck[0:5])
        self.assertEqual(13, len(self.card_deck.deck))


if __name__ == '__main__':
    unittest.main()
