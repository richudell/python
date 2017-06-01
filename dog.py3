class Animal(object):

	def __init__(self):
		print ("Animal created")
	
	def whoAmI (self):
		print ('Animal')

	def eat(self):
		print('Eating')

class Dog(object):
	def __init__(self):
		Animal.__init__(self)
		print ('Dog created')

	def whoAmI(self):
		print ('Dog')

	def bark(self):
		print ("woof!")


d = Dog()
print(d)