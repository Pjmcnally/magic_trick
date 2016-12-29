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
  
  def deal_cards(self):
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
        
  def display_cards(self):
    print("""
    Left     Cent     Right
    ----     ----    ----
    {l0}     {m0}    {r0}
    {l1}     {m1}    {r1}
    {l2}     {m2}    {r2}
    {l3}     {m3}    {r3}
    {l4}     {m4}    {r4}
    {l5}     {m5}    {r5}
    {l6}     {m6}    {r6}""".format(
      l0=self.left[0], l1=self.left[1], l2=self.left[2], l3=self.left[3], l4=self.left[4], l5=self.left[5], l6=self.left[6],
      m0=self.center[0], m1=self.center[1], m2=self.center[2], m3=self.center[3], m4=self.center[4], m5=self.center[5], m6=self.center[6],
      r0=self.right[0], r1=self.right[1], r2=self.right[2], r3=self.right[3], r4=self.right[4], r5=self.right[5], r6=self.right[6],))
  
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
    
  def pickup_cards(self):
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
      self.deal_cards()
      # self.display_cards()
      self.get_row()
      self.pickup_cards()
    else:
      self.deal_cards()
      self.display_cards()
      self.get_row()
      self.pickup_cards()


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

  print("Final Check")
  trick.deal_cards()
  trick.display_cards()
  
def main():
  do_trick()
  # check_trick()

main()
