import math

class Line(object):
	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.x1 = coor1[0]
		self.y1 = coor1[1]
		self.coor2 = coor2
		self.x2 = coor2[0]
		self.y2 = coor2[1]


	def distance(self):
		return ((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**(1/2)

	def slope(self):
		return ((self.y2 - self.y1)/(self.x2 - self.x1))

class Cylinder(object):
	def __init__(self, height=1, radius=1):
		self.height = height
		self.radius = radius

	def surfacearea(self):
		return (((2 * math.pi * self.radius)*self.height)+(2*(math.pi * self.radius**2)))

	def volume (self):
		return (math.pi * self.radius**2 * self.height)


l = Line((321,4),(9875,742))
print(l.distance())
print(l.slope())

print('*****')
c = Cylinder()
print (c.volume())
print (c.surfacearea())
