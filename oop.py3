class Dog(object):
	species = 'mammal'

	def __init__(self,breed,name, color, fur=True, pawcount=4):
		self.breed = breed
		self.name = name
		self.fur = fur
		self.color = color
		self.pawcount = pawcount

sam = Dog(breed='Lab', name = 'Sammy',color='black')
print(type(sam))
mike = Dog(breed='Huskie', name= 'Mike', color='white')
print(type(mike))
print (sam.breed)
print (sam.species)
print (sam.name)
print (sam.name + ' is a ' + sam.color + ' ' + sam.breed + ' with ' + str(sam.pawcount) + ' paws and it is ' + str(sam.fur) + ' that he has fur.')
