from math import sqrt

class Point:
	def __init__(self):
		self.x = None
		self.y = None
	def get_coords(self):
		return f"X: {self.x}; Y: {self.y}"
	def set_coords(self, x, y):
		if type(x) == int and type(y) == int:
			self.x = x
			self.y = y
		else:
			print('x и y должны быть числами')
	coords = property(get_coords, set_coords)

class Line:
	def __init__(self, a, b):
		self.p1 = p1
		self.p2 = p2
		self.length = None
	def calc_length(self):
		p1, p2 = self.p1, self.p2
		if (p1.x != None and p1.y != None) and (p2.x != None and p2.y != None):
			self.length = sqrt(abs(p2.x - p1.x)**2 + abs(p2.y - p1.y)**2)
		else:
			print('У точек неправильные координаты')

class Triangle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		self._s = None
	def get_s(self):
		return f"S = {self._s}"
	def calc_s(self):
		a, b, c = self.a.length, self.b.length, self.c.length
		if (a != None and b != None and c != None):
			p = (a + b + c)/2
			self._s = sqrt(p * (p - a) * (p - b) * (p - c))
		else:
			print("Неверные данные!")
	s = property(get_s, calc_s)

p1 = Point()
p2 = Point()
p3 = Point()

p1.set_coords(1, 2)
p2.set_coords(7, 2)
p3.set_coords(7, 8)

a = Line(p1, p2)
b = Line(p2, p3)
c = Line(p3, p1)

a.calc_length()
b.calc_length()
c.calc_length()

triangle = Triangle(a, b, c)
triangle.calc_s()

print(triangle.s)