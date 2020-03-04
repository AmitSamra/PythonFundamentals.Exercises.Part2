def greet(name):
	'''
	name is a string.
	Prints a greeting with name.
	'''
	print('Hello ' + name)

def name_input():
	'''
	choice is a user input.
	Prints a greeting with user's input.
	'''
	choice = input('Please enter a name: ')
	greet(choice)

name_input()