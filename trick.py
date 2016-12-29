def main(card):
  cards = list(range(1, 22))

  # Round 1
  left, cent, right = deal_cards(cards)
  # display_cards(left, cent, right)
  # row = input("What row is your card in (l, c, r)")
  row = find_row(card, left, cent, right)
  cards = pickup_cards(left, cent, right, row)
  
  
  # Round 2
  left, cent, right = deal_cards(cards)
  # display_cards(left, cent, right)
  # row = input("What row is your card in (l, c, r)")
  row = find_row(card, left, cent, right)
  # input("I believe your card is in the {} row.".format(row))
  cards = pickup_cards(left, cent, right, row)
 
  
  # Round 3
  left, cent, right = deal_cards(cards)
  # display_cards(left, cent, right)
  # row = input("What row is your card in (l, c, r)")
  row = find_row(card, left, cent, right)
  # input("I believe your card is in the {} row.".format(row))
  cards = pickup_cards(left, cent, right, row)

  
  # input("your card is {} the found card is {}".format(card, cards[10]))
  return card, cards[10]
  

def find_row(card, left, cent, right):
  if card in left:
    return "l"
  elif card in cent:
    return "c"
  elif card in right:
    return "r"


def display_cards(a, b, c):
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
    l0=a[0], l1=a[1], l2=a[2], l3=a[3], l4=a[4], l5=a[5], l6=a[6],
    m0=b[0], m1=b[1], m2=b[2], m3=b[3], m4=b[4], m5=b[5], m6=b[6],
    r0=c[0], r1=c[1], r2=c[2], r3=c[3], r4=c[4], r5=c[5], r6=c[6],))
  

def pickup_cards(left, cent, right, row):
  if row == "l":
    mid = left
    top = cent
    bot = right
  elif row == "c":
    mid = cent
    top = left
    bot = right
  elif row == "r":
    mid = right
    top = left
    bot = cent
  else:
    print("Error")
  
  cards = top + mid + bot
  return cards

def deal_cards(lst):
  lst_a = []
  lst_b = []
  lst_c = []
  for i, card in enumerate(lst):
    if i % 3 == 0:
      lst_a.append(card)
    elif i % 3 == 1:
      lst_b.append(card)
    elif i % 3 == 2:
      lst_c.append(card)
    else:
      print("error")
  return lst_a, lst_b, lst_c
  
for x in range(1, 22):
  goal_card, found_card = main(x)
  if goal_card == found_card:
    print("yay")
  else:
    print("boo")
    
