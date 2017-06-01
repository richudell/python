import os
os.system('cls' if os.name == 'nt' else 'clear')
import random
import time
class Di(object):
	def __init__(self, display='not initiated',value=random.randint(1,6)):
		self.display = display
		self.value = value
	def roll(self):
		number = random.randint(1,6)
		self.value = number
		self.display = str(number)
	def sum(self,dice):
		self.dice = dice
		total = 0
		for di in dice:
			total += di.value
		return total

dice = []
i=0
printdice = ''
while i < 6:
	dice.append(Di())
	dice[i].roll()
	printdice += dice[i].display + ' '
	i += 1
print (printdice)
adder=Di()
print ('You have rolled a ' + str(adder.sum(dice)))
