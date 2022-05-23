class Vehicle:
	def __init__(self, name, speed, price):
		self.name = name
		self.speed = speed
		self.price = price
		
	def info(self):
		print('Тип транспортного средства:', self.name)
		print('Максимальная скорость:', self.speed, 'км/ч')
		print('Цена:', self.price, '$')

class Car(Vehicle):
	def __init__(self, name, speed, price, color):
		Vehicle.__init__(self, name, speed, price)
		self.color = color

	def car_info(self):
		self.info()
		print('Цвет машины:', self.color, '\n')


class Airplane(Vehicle):
	def __init__(self, name, speed, price, max_height):
		Vehicle.__init__(self, name, speed, price)
		self.max_height = max_height

	def airplane_info(self):
		self.info()
		print('Максимальная высота, на которую может подняться самолёт:', self.max_height, 'метров\n')


class Ship(Vehicle):
	def __init__(self, name, speed, price, max_capacity):
		Vehicle.__init__(self, name, speed, price)
		self.max_capacity = max_capacity

	def ship_info(self):
		self.info()
		print('Количество мачт:', self.max_capacity)

myCar = Car('Машина BWM', 200, 50000, 'Чёрный')
myAirplane = Airplane('Самоёт Ту-134', 800, 1000000, 25000)
myShip = Ship('Корабль Галеон', 100, 30000, 3)

myCar.car_info()
myAirplane.airplane_info()
myShip.ship_info()
