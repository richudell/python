import os
os.system('cls' if os.name == 'nt' else 'clear')
import random
import time
class Di(object):
	def __init__(self, value=-1, display='not initiated'):
		pass

	def roll(self):
		number = random.randint(1,6)
		self.value = number
		self.display = str(number)
	def sum(self,d1,d2,d3,d4,d5,d6):
		self.d1 = d1
		self.d2 = d2
		self.d3 = d3
		self.d4 = d4
		self.d5 = d5
		self.d6 = d6
		return self.d1.value + self.d2.value + self.d3.value + self.d4.value + self.d5.value + self.d6.value

d1 = Di()
d2 = Di()
d3 = Di()
d4 = Di()
d5 = Di()
d6 = Di()

d1.roll()
d2.roll()
d3.roll()
d4.roll()
d5.roll()
d6.roll()

print (d1.display + ' ' + d2.display + ' ' + d3.display + ' ' + d4.display + ' ' + d5.display + ' ' + d6.display)
adder = Di()
print ('You have rolled a ' + str(adder.sum(d1,d2,d3,d4,d5,d6)))
