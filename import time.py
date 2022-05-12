import time
def task1(func):
	def get_time():
		start = time.time()
		func()
		end = time.time()
		print(f'Время выполнения функции {end-start} секунд')
	return get_time

@task1
def hello():
	time.sleep(1)
	print('Hello!')

hello()


def task2(func):
	def get_str(*args):
		print('Преобразование аргументов в строки...')
		for arg in args:
			arg = str(arg)
			print(arg, '-', type(arg))
		result = str(func(*args))
		print('\nПреобразование результата функции в строку...')
		print(result, '-', type(result))
	return get_str

@task2
def calc(a, b, c, d, e):
	sum_elements = a + b + c + d + e
	print('Сумма элементов =', sum_elements)
	return sum_elements

calc(1, 7, 8.2, 4, 3.8)