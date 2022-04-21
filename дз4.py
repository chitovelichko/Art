s = input('Enter the text of the word: ')
s_split = s.split(' ')

letters = "aeiouy"

words = 0

for word in s_split:
	counter = 0
	for i in word:
		if i.lower() in letters:
			counter += 1
		else:
			counter = 0
		if counter == 2:
			words += 1;
			break

        #########

shops = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}

min_num = float(input('Enter the minimum price: '))
max_num = float(input('Enter the maximum price: '))

valid_shops = []

for s in shops.items():
	if s[1] >= min_num and s[1] <= max_num:
		valid_shops.append(s[0])

print('shops:', valid_shops)
