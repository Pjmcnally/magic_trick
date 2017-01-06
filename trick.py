""" Next step is to continue OOP 

I may need a deck object later.

I may also want card objects later (simple ints are fine for now).

"""

from random import shuffle, sample # in 3.6 sample becomes choices

class Trick():
  def __init__(self, card=None):
    self.card = card
    self.deck = list(range(1, 22))
    self.left = []
    self.center = []
    self.right = []
    self.row = ""
    self.piles = {}
  
  def deal_rows(self):
    self.left = []
    self.center = []
    self.right = []
    
    for i, card in enumerate(self.deck):
      if i % 3 == 0:
        self.left.append(card)
      elif i % 3 == 1:
        self.center.append(card)
      elif i % 3 == 2:
        self.right.append(card)
      else:
        print("error")
        
  def display_rows(self):
    print("""
    Left     Cent     Right
    ----     ----    ----
    {:<4}     {:^4}    {:>4}
    {:<4}     {:^4}    {:>4}
    {:<4}     {:^4}    {:>4}
    {:<4}     {:^4}    {:>4}
    {:<4}     {:^4}    {:>4}
    {:<4}     {:^4}    {:>4}
    {:<4}     {:^4}    {:>4}""".format(
      self.left[0], self.center[0], self.right[0],
      self.left[1], self.center[1], self.right[1],
      self.left[2], self.center[2], self.right[2],
      self.left[3], self.center[3], self.right[3],
      self.left[4], self.center[4], self.right[4],
      self.left[5], self.center[5], self.right[5],
      self.left[6], self.center[6], self.right[6])
    )
  
  def get_row(self):
    if self.card:
      if self.card in self.left:
        self.row = "l"
        return True
      elif self.card in self.right:
        self.row = "r"
        return True
      elif self.card in self.center:
        self.row = "c"
        return True
    else:
      self.row = input("What row is your card in (l, c, r)")
      return True
    
  def pickup_rows(self):
    if self.row == "l":
      mid = self.left
      top, bot = sample([self.center, self.right], 2)
    elif self.row == "c":
      mid = self.center
      top, bot = sample([self.left, self.right], 2)
    elif self.row == "r":
      mid = self.right
      top, bot = sample([self.left, self.center], 2)
    else:
      print("Error")
      
    shuffle(top)
    shuffle(bot)
    
    self.deck = top + mid + bot
    
  def round(self):
    if self.card:
      self.deal_rows()
      # self.display_rows()
      self.get_row()
      self.pickup_rows()
    else:
      self.deal_rows()
      self.display_rows()
      self.get_row()
      self.pickup_rows()
      
  def part_2(self):
    self.card = self.deck[10]
    print("Card = ", self.card)
    self.build_piles()
    print("Piles = ", self.piles)
    while (len(self.piles) > 1):
      self.display_piles()
      pile = self.get_pile()
      self.pile_magic(pile)
    print(self.piles)
      
  def build_piles(self):
    del self.deck[20] #  Remove last card in deck to get deck down to 20 cards
    shuffle(self.deck)
    pile = 1
    count = 0 
    for x in self.deck:
      temp = self.piles.get(pile, [])
      temp.append(x)
      self.piles[pile] = temp
      count += 1
      if count == 4:
        count = 0
        pile += 1
    
  def display_piles(self):
    for key, value in self.piles.items():
      print(key)
      
  def get_pile(self):
    while True:
      pile = int(input("Please select a pile (enter the number)"))
      if pile in self.piles.keys():
        return pile
      else:
        print("That is not a valid pile")
        
  def pile_magic(self, pile):
    if self.card in self.piles[pile]:
      print("That pile is full of magic.  You were right to keep it.")
      temp = self.piles[pile]
      self.piles.clear()
      self.piles[pile] = temp
    else:
      print("That pile is without magic.  You were right to remove it.")
      del self.piles[pile]
    

def check_trick():
  for x in range(1, 22):
    trick = Trick(x)
    trick.round()  # Round 1
    trick.round()  # Round 2
    trick.round()  # Round 3
  
    # Check
    # print("Final Check")
    # trick.deal_cards()
    if trick.card == trick.deck[10]:
      print("Yay!")
    else:
      print("Boo!")

def do_trick():
  trick = Trick()
  trick.round()  # Round 1
  trick.round()  # Round 2
  trick.round()  # Round 3

  trick.part_2()
  
  # print("Final Check")
  # print("Your Card is {}".format(trick.card))
  
def main():
  do_trick()
  # check_trick()

main()
