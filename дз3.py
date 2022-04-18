word = input('Enter a word: ')
num = int(input(f'Enter a num (max {len(word)}): '))

print(f'The {num} symbol in "{word}" is {word[num-1]}')

#######
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8]
lst2 = []

for element in lst1:
	if type(element) == int:
		lst2.append(element)

print('lst1 -', lst1)
print('lst2 -', lst2)
#####
words = input('Enter a string of words separated by a space: ');

words_arr = words.split(' ')
words_count = 0
for word in words_arr:
	if word.isalpha():
		words_count += 1;

print(f'You entered {words_count} words')


