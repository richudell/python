import os
os.system('cls' if os.name == 'nt' else 'clear')
import random
import time
class Player(object):
	def __init__ (self, name, hair, eyes, sex, bankroll=100, cash=100):
		self.name = name
		self.hair = hair
		self.eyes = eyes
		self.sex = sex
		self.bankroll = bankroll
		self.cash = cash

	def addBankroll(self, money):
		self.bankroll += money

	def cashOut(self):
		loot = self.bankroll
		self.bankroll = 0
		self.cash = self.cash + loot
		return 'Cashing out $' + str(loot) + '.  Congratulations!  Your current cash is $' + str(self.cash) + '.'

class Deck(object):
	deck = []
	cards = []
	values = []
	class Card(object):
		def __init__ (self,card,suit):
			self.card = card
			self.suit = suit
			if self.card == 'Ace':
				self.value = 1
			elif self.card == '2':
				self.value = 2
			elif self.card == '3':
				self.value = 3
			elif self.card == '4':
				self.value = 4
			elif self.card == '5':
				self.value = 5
			elif self.card == '6':
				self.value = 6
			elif self.card == '7':
				self.value = 7
			elif self.card == '8':
				self.value = 8
			elif self.card == '9':
				self.value = 9
			else:
				self.value = 10		
	for card in ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'):
		for suit in ('Spades','Clubs','Diamonds','Hearts'):
			c = Card(card,suit)
			cards.append(c)

	def __init__ (self):
		pass

	def shuffle (self):
		print('Shuffling...')
		random.shuffle(self.cards)
		time.sleep(1.1)


class PlayerHand(object):
	def __init__ (self,Player,cards=[]):
		self.Player=Player
		self.cards=cards

	def Points (self,player,checkonly):
		self.player=player
		self.checkonly=checkonly
		totalpoints = sum(i.value for i in self.cards if self.Player==self.player)
		if totalpoints > 21 and self.checkonly == False:
			print (player.name.capitalize() + ' has BUST!!!')
		return totalpoints
	def Add (self,card):
		self.cards.append(card)
			
class DealerHand(object):
	def __init__ (self,Player,cards=[]):
		self.Player=Player
		self.cards=cards

	def Points (self,player,checkonly):
		self.player=player
		self.checkonly=checkonly
		##for p in self.cards:
		#	print(p.value)
		totalpoints = sum(i.value for i in self.cards if self.Player==self.player)
		if totalpoints > 21 and self.checkonly == False:
			print (player.name.capitalize() + ' has BUST!!!')
		return totalpoints
	def Add (self,card):
		self.cards.append(card)
			

sam = Player(name = 'sam',hair = 'blonde', eyes='green', sex='M')
sam.addBankroll(50)
dealer = Player(name = 'mike',hair = 'black', eyes='brown', sex='M')

samHand = PlayerHand(sam)
dealerHand = DealerHand(dealer)

print(sam.cashOut())
d = Deck()
# print (d.cards)
print('*******************************************')
shuffleCount = random.randint(2,5)
for m in range(shuffleCount):

	d.shuffle()

# print (d.cards)
# print('**************************************')
#for i in d.cards:
#	print (str(i.card) + ' of ' + i.suit + ' is worth ' +str(i.value))
samHand.Add(d.cards.pop())
dealerHand.Add(d.cards.pop())
samHand.Add(d.cards.pop())
dealerHand.Add(d.cards.pop())

print('************************************************')
print ('Sam                             Dealer')
print(samHand.cards[0].card + ' of ' + samHand.cards[0].suit + " "*(28-len(samHand.cards[0].card)-len(samHand.cards[0].suit)) + dealerHand.cards[0].card + ' of ' + dealerHand.cards[0].suit)
print(samHand.cards[1].card + ' of ' + samHand.cards[1].suit + " "*(28-len(samHand.cards[1].card)-len(samHand.cards[1].suit)) + '-----')
a = input('H to hit, S to stay: ')
print('************************************************')
print(samHand.cards[0].card + ' of ' + samHand.cards[0].suit + " "*(28-len(samHand.cards[0].card)-len(samHand.cards[0].suit)) + dealerHand.cards[0].card + ' of ' + dealerHand.cards[0].suit)
print(samHand.cards[1].card + ' of ' + samHand.cards[1].suit + " "*(28-len(samHand.cards[1].card)-len(samHand.cards[1].suit)) + '-----')
incrementer = 2
while a == 'H':
	samHand.Add(d.cards.pop())
	print('************************************************')
	looper = 0
	for allCards in samHand.cards:
		current = allCards.card + ' of ' + allCards.suit + " "*(28-len(allCards.card) - len(allCards.suit))
		# print ('***' + str(len(dealerHand.cards)))
		if len(dealerHand.cards)-1 > looper:
			current += dealerHand.cards[looper].card + ' of ' + dealerHand.cards[looper].suit
		elif looper == 1:
			current += '-----'
		print(current)
		looper += 1
	if samHand.Points(sam,True)>21:
		break
	incrementer += 1
	a = input ('H to hit, S to stay: ')


while dealerHand.Points(dealer,False) < 17:
	if samHand.Points(sam,False) > 21:
		break
	dealerHand.Add(d.cards.pop())
	print('************************************************')
	looper = 0
	if len(samHand.cards) >=len(dealerHand.cards):
		for allCards in samHand.cards:
			current = allCards.card + ' of ' + allCards.suit + " "*(28-len(allCards.card) - len(allCards.suit))
			# print ('***' + str(len(dealerHand.cards)))
			if len(dealerHand.cards) > looper:
				current += dealerHand.cards[looper].card + ' of ' + dealerHand.cards[looper].suit
			elif looper == 1:
				current += '-----'
			print(current)
			looper += 1
		
		incrementer += 1
print('************************************************')
looper = 0
if len(samHand.cards) > len(dealerHand.cards):
	for allCards in samHand.cards:
		if len(samHand.cards) > looper:
			current = allCards.card + ' of ' + allCards.suit + " "*(28-len(allCards.card) - len(allCards.suit))
		else:
			current = ' '*28
		if len(dealerHand.cards) > looper:
			current += dealerHand.cards[looper].card + ' of ' + dealerHand.cards[looper].suit
		print(current)
		looper += 1
else:
	for allCards in dealerHand.cards:
		if len(dealerHand.cards) > looper:
			current = allCards.card + ' of ' + allCards.suit
		if len(samHand.cards) > looper:
			current = samHand.cards[looper].card + ' of ' + samHand.cards[looper].suit + " "*(33-len(samHand.cards[looper].card + ' of ' + samHand.cards[looper].suit)) + current
		else:
			current = ' '*33 + current
		print(current)
		looper += 1
samHand.Points(sam,False)
dealerHand.Points(dealer,False)
if samHand.Points(sam, True)<22:
	if dealerHand.Points(dealer, True) < samHand.Points(sam, True) or dealerHand.Points(dealer, True) > 21:
		print(sam.name.capitalize() + ' has won!')
	elif dealerHand.Points(dealer, True) < 22:
		print(dealer.name.capitalize() + ' has won!')
	else:
		print('Draw!')
else:
	print(dealer.name.capitalize() + ' has won!')
