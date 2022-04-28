#Напишіть функцію, що приймає один аргумант. Функція має вивести на ектан тип цього аргумента
def task1(x):
	print('\nTask 1')
	print(f'Arg - {x}. type - {type(x)}')

task1(8.4)

##Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
##Якщо перетворити не вдається функція має повернути 0.

def task2(x):
	if type(x) == int:
		return float(x)
	else:
		return 0

print('\nTask 2')
print(task2("str"))
print(task2(8))

###Напишіть функцію, що приймає два аргументи. Функція повинна:
#якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
#якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
#якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
#у будь-якому іншому випадку повернути кортеж з цих аргументів

def task3(x, y):
	if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
		return x-y
	elif type(x) == str and type(y) == str:
		return x+y
	elif type(x) == str and type(y) != str:
		return {x: y}
	else:
		return (x, y)

print('\nTask 3')
print(task3(2, 2.3))
print(task3("hello", "world"))
print(task3("hello", True))
print(task3(True, 5.4))
