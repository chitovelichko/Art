from random import choice

WIN_RULES = {
'stone': ['scissors', 'lizard'],
'paper': ['stone', 'spouk'],
'scissors': ['paper', 'lizard'],
'spouk': ['scissors', 'stone'],
'lizard': ['spouk', 'paper']
}

# get data from user
def get_user_choice():
	while True:
		user_choice = input('Enter your choice (stone paper scissors lizard spouk): ')
		if user_choice not in WIN_RULES.keys():
			print('Enter only: stone paper scissors')
			continue
		else:
			return user_choice

# get data from computer
def get_computer_choice():
	computer_choice = choice(list(WIN_RULES.keys()))
	return computer_choice

# # define winner
def get_winner(user_choice, computer_choice):
	if user_choice == computer_choice:
		msg = 'Draw'
	elif computer_choice in WIN_RULES[user_choice]:
		msg = 'User'
	else:
		msg = 'Computer'
	return msg

# make message
def make_message(user_choice, computer_choice, winner):
	msg = f'User choice is {user_choice}, PC choice is {computer_choice}. Winner is {winner}'
