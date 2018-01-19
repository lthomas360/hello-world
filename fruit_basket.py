def guess_fruit(fruit_basket):
	guess = raw_input('Guess a fruit from the basket:')
	if guess in fruit_basket:
		print('Your Guess is correct!')

def main():
	fruit_basket = ['apple','banana','orange','avocado','blueberry']
	guess_fruit(fruit_basket)

main()