#deck of cards
import random

class Card:
  def __init__ (self, suit, value):
    self.suit = suit
    self.value = value
  def show(self):
    print(f"{self.value} of {self.suit}")

class Deck:
  def __init__ (self):
    self.cards = []
    self.build()
  def build(self):
    for s in ["Diamond","Clubs","Heart","Spade"]:
      for v in range(1,14):
        self.cards.append(Card(s,v))
  def show(self):
    for c in self.cards:
      c.show()
  def shuffle(self):
    for i in range(len(self.cards)-1,0,-1):
      r = random.randint(0,i)
      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
  def draw_card(self):
    return self.cards.pop()


class Player:
  def __init__(self,name):
    self.name = name
    self.hand = []
  def draw(self, Deck):
    self.hand.append(deck.draw_card())
  def showHand(self):
    for card in self.hand:
      card.show()

deck = Deck()
deck.shuffle()

jansoy = Player("Jansoy")
jansoy.draw(Deck)
jansoy.showHand()
