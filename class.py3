import math

class Circle(object):
	pi = math.pi

	def __init__(self,radius=1):
		self.radius = radius

	def area(self):
		return Circle.pi*self.radius**2

	def set_radius(self,new_radius):
		"""
		This method takes in a new radius
		"""
		self.radius = new_radius

	def get_radius (self):
		return self.radius

	def get_perimeter (self):
		return 2*Circle.pi*self.radius



c=Circle(100)
c.set_radius(20)
print (c.area())
print (c.get_radius())
print (c.get_perimeter())