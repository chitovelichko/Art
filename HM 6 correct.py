def get_age():
	"""Введення віку"""
	return int(input('Введіть ваш вік: '))

def get_age_form(age):
	"""Перевірка на падеж для слова 'рік'"""
	numbers_1 = [2, 3, 4]
	numbers_2 = [5, 6, 7, 8, 9, 0]
	if age % 10 == 1:
		return 'рік'
	elif (age >= 5 and age <= 20) or age % 10 in numbers_2:
		return 'років'
	elif (age % 10 in numbers_1):
		return 'роки'

def check_age(age):
	"""Перевірка віку"""
	if age < 7:
		return f'Тобі же {age} {get_age_form(age)}! Где твої батьки?'
	elif age < 16:
		return f'Тобі тільки {age} {get_age_form(age)}, а цей фільм для дорослих!'
	elif age % 10 == age // 10:
		return f'О, вам {age} {get_age_form(age)}! Який цікавий вік'
	elif age > 65:
		return f'Вам {age} {get_age_form(age)}? Покажите пенсионное удостоверение!'
	else:
		return f'Несмотря на то, что вам {age} {get_age_form(age)}, билетов все равно нет.'

age = get_age()
print(check_age(age))

