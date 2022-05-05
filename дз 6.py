def get_age():
	"""Ввод возраста"""
	return int(input('Введите ваш возраст: '))

def get_age_form(age):
	"""Проверка на падеж для слова 'год'"""
	numbers_1 = [2, 3, 4]
	numbers_2 = [5, 6, 7, 8, 9, 0]
	if age % 10 == 1:
		return 'год'
	elif (age >= 5 and age <= 20) or age % 10 in numbers_2:
		return 'лет'
	elif (age % 10 in numbers_1):
		return 'года'

def check_age(age):
	"""Проверка возраста"""
	if age < 7:
		return f'Тебе же {age} {get_age_form(age)}! Где твои родители?'
	elif age < 16:
		return f'Тебе только {age} {get_age_form(age)}, а это фильм для взрослых!'
	elif age % 10 == age // 10:
		return f'О, вам {age} {get_age_form(age)}! Какой интересный возраст'
	elif age > 65:
		return f'Вам {age} {get_age_form(age)}? Покажите пенсионное удостоверение!'
	else:
		return f'Несмотря на то, что вам {age} {get_age_form(age)}, билетов все равно нет.'

age = get_age()
print(check_age(age))

